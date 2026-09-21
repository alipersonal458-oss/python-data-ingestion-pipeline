import os
import logging
import requests
import pandas as pd
from dotenv import load_dotenv

# 1. Logging Setup (File + Terminal Output)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("pipeline.log"),  # pipeline.log file mein save hoga
        logging.StreamHandler()               # Terminal screen par show hoga
    ]
)

# 2. Environment Variables Load Karein
load_dotenv()
API_URL = os.getenv("BASE_API_URL", "https://jsonplaceholder.typicode.com/posts")

def fetch_data():
    """Defensive API Data Extraction"""
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
    """Pandas Automated Data Cleaning & Normalization"""
    if not raw_data:
        logging.warning("No data received for transformation.")
        return None

    logging.info("Cleaning and transforming data with Pandas...")
    
    # Raw JSON ko Pandas DataFrame (Table) mein convert karein
    df = pd.DataFrame(raw_data)

    # Clean 1: Duplicates Remove Karein
    initial_count = len(df)
    df.drop_duplicates(inplace=True)
    logging.info(f"Removed duplicates: {initial_count - len(df)} rows dropped.")

    # Clean 2: Missing/Null Values Fill Karein
    df.fillna({"title": "Unknown Title", "body": "No Content"}, inplace=True)

    # Clean 3: Text Formatting (Extra spaces hatana)
    if "title" in df.columns:
        df["title"] = df["title"].str.strip()
    if "body" in df.columns:
            df["body"] = df["body"].str.strip()
    

    logging.info("Data transformation completed successfully.")
    return df

def save_to_csv(df, filename="fetch_data.csv"):
    """Persist Cleaned Data to CSV"""
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