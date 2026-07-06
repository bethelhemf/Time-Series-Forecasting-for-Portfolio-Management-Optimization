# scripts/config.py
from pathlib import Path

# 1. Path Settings
# This finds the project root regardless of which PC you are on
BASE_DIR = Path(__file__).resolve().parent.parent

# Path to the processed data CSV
# This matches your folder structure: portfolio-optimization/data/processed/
DATA_PATH = BASE_DIR / "data" / "processed" / "raw_stock_data.csv"

# 2. Forecasting Settings
TARGET_ASSET = 'TSLA'
TRAIN_END_DATE = '2024-12-31'
TEST_START_DATE = '2025-01-01'

# 3. Model Hyperparameters (For Task 2)
WINDOW_SIZE = 60
LSTM_UNITS = 50
DROPOUT_RATE = 0.2
EPOCHS = 10
BATCH_SIZE = 32

# 4. Risk Settings (For Task 3)
RISK_FREE_RATE = 0.02

# scripts/config.py (Add these lines)
FORECAST_HORIZON = 252  # ~12 months of trading days
CONFIDENCE_LEVEL = 0.95