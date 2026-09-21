# 📊 Live API Data Ingestion Pipeline

A production-grade Python-based Data Engineering ingestion pipeline designed to dynamically fetch live JSON data from REST APIs, clean/normalize nested payloads, and safely persist structured outputs into CSV format.

---

## 🏗 Architecture & Workflow

[ External REST API ] ──(HTTP GET / Defensive Requests)──> [ Python Ingestion Script ] ──(Data Cleaning & Normalization)──> [ Local CSV Storage ]


---

## ✨ Key Features

- **🛡 Defensive HTTP Requests:** Integrated robust exception handling using `requests` (`HTTPError`, `ConnectionError`, `Timeout`) to ensure resilient execution.
- **🔐 Secret & Environment Security:** Managed dynamic configuration endpoints via `.env` files and `python-dotenv` to eliminate hardcoded credentials.
- **🧹 Payload Normalization:** Parsed complex API JSON structures into clean tabular rows ready for downstream analytics.
- **📁 Safe Storage:** Structured automated exporting to CSV using Python's built-in `csv` library.

---

## 🛠 Tech Stack

- **Language:** Python 3.11+
- **Libraries:** `requests`, `python-dotenv`
- **Version Control:** Git & GitHub

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/alipersonal458-oss/python-data-ingestion-pipeline.git](https://github.com/alipersonal458-oss/python-data-ingestion-pipeline.git)
cd python-data-ingestion-pipeline