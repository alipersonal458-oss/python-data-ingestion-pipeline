import logging
import pandas as pd

def clean_and_transform_data(raw_data):
    """Clean missing values, drop duplicates, and format string fields."""
    if not raw_data:
        logging.warning("No data received for transformation.")
        return None

    logging.info("Cleaning and transforming data with Pandas...")
    
    # Convert incoming JSON list into a Pandas DataFrame
    df = pd.DataFrame(raw_data)

    # Remove identical records
    initial_count = len(df)
    df.drop_duplicates(inplace=True)
    logging.info(f"Removed duplicates: {initial_count - len(df)} rows dropped.")

    # Fill blank text fields with sensible defaults
    df.fillna({"title": "Unknown Title", "body": "No Content"}, inplace=True)

    # Strip unwanted whitespace from string columns
    if "title" in df.columns:
        df["title"] = df["title"].str.strip()
    if "body" in df.columns:
        df["body"] = df["body"].str.strip()

    logging.info("Data transformation completed successfully.")
    return df