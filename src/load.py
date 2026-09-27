import sqlite3
import logging

DB_NAME = "pipeline_data.db"

def load_data_to_sqlite(df):
    """Load cleaned DataFrame into SQLite relational database with proper schema."""
    if df is None or df.empty:
        logging.error("Failed to load: DataFrame is empty or None.")
        return False

    logging.info("Starting database loading operation...")
    
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            
            # Enable Foreign Keys
            cursor.execute("PRAGMA foreign_keys = ON;")
            
            # Create Table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY,
                userId INTEGER NOT NULL,
                title TEXT NOT NULL,
                body TEXT NOT NULL
            )
            """)
            
            # Insert or Ignore for idempotency/duplicates
            records = df[['id', 'userId', 'title', 'body']].to_dict(orient='records')
            
            cursor.executemany("""
            INSERT OR IGNORE INTO posts (id, userId, title, body)
            VALUES (:id, :userId, :title, :body)
            """, records)
            
            logging.info(f"Successfully loaded {cursor.rowcount} records into SQLite database '{DB_NAME}'.")
            return True

    except sqlite3.Error as e:
        logging.error(f"Database insertion error: {e}")
        return False