# First-Time Setup Guide

**Project**: payments-data-lake-foundations

## 1. Prerequisites
- Python 3.11 or higher
- Git
- (Optional) VS Code with Python + Ruff extensions

## 2. Clone the Repository
```bash
git clone https://github.com/ginko97/payments-data-lake-foundations.git
cd payments-data-lake-foundations

## 3. Install uv
bash
curl -LsSf https://astral.sh/uv/install.sh | sh

PowerShell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

## 4. Setup Project Environment

Install dependencies + create .venv
uv sync

Generate raw data (Bronze layer)
uv run -m src.ingestion.generate_data

Transform to Silver layer
uv run -m src.transform.bronze_to_silver

