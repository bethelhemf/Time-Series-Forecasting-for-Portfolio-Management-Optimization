# src/data_loader.py
import pandas as pd
import logging
from pathlib import Path

def load_processed_data(file_path: Path) -> pd.DataFrame:
    """Loads CSV data with error handling."""
    if not file_path.exists():
        logging.error(f"File not found at {file_path}")
        raise FileNotFoundError(f"Could not find processed data at: {file_path}")
    
    df = pd.read_csv(file_path, parse_dates=['Date'])
    return df

def split_data_chronologically(df: pd.DataFrame, asset: str, train_end: str, test_start: str):
    """Splits a dataframe into training and testing sets based on dates."""
    # Ensure Date is index
    if 'Date' in df.columns:
        df = df.set_index('Date')
    
    series = df[asset].dropna()
    train = series.loc[:train_end]
    test = series.loc[test_start:]
    
    return train, test