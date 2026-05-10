from src.utils.config import settings
from src.utils.logger import logger
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

def generate_synthetic_payments(num_records: int = 150_000):
    logger.info("Starting synthetic payments generation", num_records=num_records)
    
    # Ensure directories exist
    settings.data_raw_path.mkdir(parents=True, exist_ok=True)
    
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=7)
    
    df = pd.DataFrame({
        "transaction_id": [f"TX-{i:010d}" for i in range(num_records)],
        "timestamp": pd.date_range(start=start_date, periods=num_records, freq="s"),
        "user_id": np.random.randint(1000, 99999, num_records),
        "merchant_id": np.random.randint(100, 9999, num_records),
        "amount": np.round(np.random.lognormal(4, 1.5, num_records), 2),
        "currency": np.random.choice(["USD", "EUR", "SGD"], num_records),
        "status": np.random.choice(["success", "failed", "pending"], num_records, p=[0.92, 0.05, 0.03]),
        "payment_method": np.random.choice(["card", "wallet", "bank"], num_records),
    })
    
    # Save as partitioned Parquet
    partition_date = df["timestamp"].dt.date.iloc[0].strftime("%Y-%m-%d")
    output_path = settings.data_raw_path / f"date={partition_date}"
    output_path.mkdir(parents=True, exist_ok=True)
    
    df.to_parquet(output_path / "payments_raw.parquet", compression="snappy")
    
    logger.info("✅ Raw payments data generated", 
                records=num_records, 
                path=str(output_path))
    return df

def main():
    generate_synthetic_payments()

if __name__ == "__main__":
    generate_synthetic_payments()
    main()