# Modular Automated Data Ingestion & ETL Pipeline

A production-grade, modular Python ETL pipeline that securely extracts data from a REST API, performs automated cleaning and transformation using Pandas, and idempotently loads data into an SQLite relational database.

## 🚀 Key Features

- **Defensive API Extraction:** Safe HTTP requests with error handling (`src/extract.py`).
- **Data Transformation:** Pandas-driven duplicate removal, missing value imputation, and type normalization (`src/transform.py`).
- **Idempotent Relational Storage:** SQLite integration with foreign keys enabled and `INSERT OR IGNORE` batch loading using named parameters (`src/load.py`).
- **Modular Architecture:** Professional `src/` modularization orchestrated centrally via `main.py`.
- **Structured Logging:** Dual-handler logging outputs pipeline execution status to both console and `pipeline.log`.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Data Processing:** `pandas`
- **Database:** SQLite3
- **Tooling & API:** `requests`, `python-dotenv`, Git, GitHub

## 📁 Project Structure

```text
PROJECT/
├── src/
│   ├── extract.py         # REST API data extraction module
│   ├── transform.py       # Pandas data cleaning & transformation logic
│   └── load.py            # SQLite relational database loading module
├── main.py                # Pipeline execution orchestrator
├── .env                   # Environment variables (Git-ignored)
├── .env.example           # Shared environment template
├── .gitignore             # Git exclusions
└── README.md              # Project documentation