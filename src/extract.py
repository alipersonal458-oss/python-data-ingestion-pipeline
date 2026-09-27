import os
import logging
import requests
from dotenv import load_dotenv

# Load environment configuration
load_dotenv()
API_URL = os.getenv("BASE_API_URL", "https://jsonplaceholder.typicode.com/posts")

def fetch_data():
    """Fetch raw JSON payload from the API with timeout and error handling."""
    logging.info("Starting API data extraction...")
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        logging.info("Data successfully fetched from API!")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"API Request Failed: {e}")
        return None