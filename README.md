# payments-data-lake-foundations

**Week 1-2 Project** — Fintech Payments Data Lake Foundations  

---

## Project Goal
Build a clean **Medallion Architecture** (Bronze → Silver) using synthetic payment transactions — the foundation of real-time fraud detection and risk scoring systems.

## Architecture Overview

## Tech Stack
- Python 3.11 + uv
- Pandas + PyArrow
- Parquet (Snappy compression)
- DuckDB (local SQL analytics)
- Pydantic + structlog (production config & logging)

## Project Structure
```bash
payments-data-lake-foundations/
├── src/
│   ├── ingestion/           # Raw data generation
│   ├── transform/           # Bronze → Silver
│   └── utils/               # config + logger
├── data/
│   ├── raw/
│   ├── bronze/
│   └── silver/
├── notebooks/               # SQL analysis + certification practice
├── tests/
├── docs/
├── pyproject.toml
└── README.md