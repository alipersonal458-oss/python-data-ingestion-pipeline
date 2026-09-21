import os
import logging
import requests
import pandas as pd
from dotenv import load_dotenv

# Configure logging to output both to a log file and the terminal
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("pipeline.log"),  # Saves logs locally
        logging.StreamHandler()               # Prints logs directly to console
    ]
)

# Load environment configuration
load_dotenv()
API_URL = os.getenv("BASE_API_URL", "[https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts)")

def fetch_data():
    """Fetch raw JSON payload from the API with basic error handling."""
    logging.info("Starting API data extraction...")
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        logging.info("Data successfully fetched from API!")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"API Request Failed: {e}")
        return None

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

def save_to_csv(df, filename="fetch_data.csv"):
    """Save the cleaned DataFrame to a CSV file."""
    if df is not None:
        df.to_csv(filename, index=False)
        logging.info(f"Cleaned dataset saved to {filename}")
    else:
        logging.error("Failed to save: DataFrame is empty.")

if __name__ == "__main__":
    logging.info("=== Starting Pipeline Execution ===")
    data = fetch_data()
    cleaned_df = clean_and_transform_data(data)
    save_to_csv(cleaned_df)
    logging.info("=== Pipeline Execution Finished ===")