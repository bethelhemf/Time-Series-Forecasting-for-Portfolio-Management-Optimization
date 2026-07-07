# scripts/config.py
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed" / "raw_stock_data.csv"

# Model Hyperparameters
WINDOW_SIZE = 60
TRAIN_SPLIT_DATE = '2024-12-31'
TEST_START_DATE = '2025-01-01'

# LSTM Settings
LSTM_UNITS = 50
DROPOUT_RATE = 0.2
EPOCHS = 10
BATCH_SIZE = 32

# scripts/config.py
from pathlib import Path

# Data Paths
RAW_DATA_FILE = "raw_stock_data.csv"
PROCESSED_DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "processed"

# Model Settings
TARGET_ASSET = 'TSLA'
TRAIN_END_DATE = '2024-12-31'
TEST_START_DATE = '2025-01-01'

# scripts/config.py (Add these)
RISK_FREE_RATE = 0.02  # Current approx 10-year Treasury yield
PORTFOLIO_TICKERS = ['TSLA', 'BND', 'SPY']