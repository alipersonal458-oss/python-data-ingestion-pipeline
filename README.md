# Automated Data Ingestion & Transformation Pipeline

A production-grade Python data pipeline that securely extracts data from a REST API, performs automated cleaning and transformation using Pandas, and logs execution metrics for monitoring.

## 🚀 Key Features

- **Defensive API Extraction:** Safe HTTP requests with timeout and error handling.
- **Environment Security:** API endpoints managed securely via `.env` environment variables.
- **Automated Data Cleaning:** Pandas-driven duplicate removal, missing value imputation, and string normalization.
- **Structured Logging:** Simultaneous console and file-based execution logging (`pipeline.log`).
- **Modular Architecture:** Clean functional design with standard `if __name__ == "__main__":` entry point.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:** `pandas`, `requests`, `python-dotenv`
- **Tooling:** Git, GitHub, VS Code

## 📁 Project Structure

```text
PROJECT/
├── Data_Ingestion_Pipeline_Project.py  # Main pipeline logic
├── .env                                # Environment variables (Git-ignored)
├── .env.example                        # Template for environment configuration
├── pipeline.log                        # Execution logs
├── fetch_data.csv                      # Processed dataset output
├── .gitignore                          # Excluded files
└── README.md                           # Project documentation
```