import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models, expected_returns

def calculate_covariance(returns_df):
    """Calculates the annualized sample covariance matrix."""
    return risk_models.sample_cov(returns_df)

def plot_covariance_heatmap(cov_matrix):
    """Generates a professional heatmap for the covariance matrix."""
    plt.figure(figsize=(8, 6))
    sns.heatmap(cov_matrix, annot=True, cmap='viridis', fmt='.4f')
    plt.title("Figure 7. Asset Covariance Matrix Heatmap")
    plt.show()

def run_optimization(expected_returns_series, cov_matrix, risk_free_rate=0.02):
    """
    Runs MPT optimization to find Max Sharpe and Min Volatility portfolios.
    """
    # Max Sharpe Ratio (Tangency Portfolio)
    ef_sharpe = EfficientFrontier(expected_returns_series, cov_matrix)
    weights_sharpe = ef_sharpe.max_sharpe(risk_free_rate=risk_free_rate)
    perf_sharpe = ef_sharpe.portfolio_performance(verbose=False, risk_free_rate=risk_free_rate)

    # Minimum Volatility Portfolio
    ef_vol = EfficientFrontier(expected_returns_series, cov_matrix)
    weights_vol = ef_vol.min_volatility()
    perf_vol = ef_vol.portfolio_performance(verbose=False, risk_free_rate=risk_free_rate)

    return {
        "Max Sharpe": {"weights": weights_sharpe, "perf": perf_sharpe},
        "Min Volatility": {"weights": weights_vol, "perf": perf_vol}
    }