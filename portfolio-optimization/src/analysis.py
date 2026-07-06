# src/analysis.py
import numpy as np
import pandas as pd

def generate_future_dates(last_date, n_steps):
    """Generates future trading dates (excluding weekends)."""
    return pd.date_range(start=last_date, periods=n_steps + 1, freq='B')[1:]

def calculate_confidence_intervals(forecast_series, sigma, n_steps):
    """
    Manually calculates growing uncertainty for ML models.
    In finance, uncertainty usually grows with the square root of time.
    """
    intervals = []
    for t in range(1, n_steps + 1):
        bound = 1.96 * sigma * np.sqrt(t) # 95% confidence interval
        intervals.append(bound)
    
    lower_bound = forecast_series - np.array(intervals)
    upper_bound = forecast_series + np.array(intervals)
    return lower_bound, upper_bound