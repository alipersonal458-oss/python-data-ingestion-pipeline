import logging
from src.extract import fetch_data
from src.transform import clean_and_transform_data
from src.load import load_data_to_sqlite

# Configure logging to output both to a log file and the terminal
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("PROJECT/pipeline.log"),  # Saves logs locally
        logging.StreamHandler()               # Prints logs directly to console
    ]
)

def run_pipeline():
    """Orchestrate the modular ETL pipeline steps."""
    logging.info("=== Starting ETL Pipeline Execution ===")
    
    # 1. Extract
    raw_data = fetch_data()
    if not raw_data:
        logging.error("Pipeline aborted: Extraction failed.")
        return

    # 2. Transform
    cleaned_df = clean_and_transform_data(raw_data)
    if cleaned_df is None:
        logging.error("Pipeline aborted: Transformation failed.")
        return

    # 3. Load
    success = load_data_to_sqlite(cleaned_df)
    if success:
        logging.info("=== ETL Pipeline Execution Completed Successfully ===")
    else:
        logging.error("=== ETL Pipeline Execution Failed At Loading Stage ===")

if __name__ == "__main__":
    run_pipeline()