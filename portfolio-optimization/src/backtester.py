# src/backtester.py
import pandas as pd
import numpy as np

def run_backtest_simulation(returns_df, weights):
    """
    Calculates cumulative returns and daily portfolio returns.
    """
    # Ensure weights is a pandas series
    if not isinstance(weights, pd.Series):
        weights = pd.Series(weights)
        
    daily_rets = (returns_df * weights).sum(axis=1)
    cum_rets = (1 + daily_rets).cumprod()
    return cum_rets, daily_rets

def get_performance_metrics(daily_returns, risk_free_rate=0.02):
    """
    Calculates Total Return, Annualized Return, Sharpe Ratio, and Max Drawdown.
    """
    total_return = (1 + daily_returns).prod() - 1
    ann_return = daily_returns.mean() * 252
    ann_vol = daily_returns.std() * np.sqrt(252)
    
    # Handle division by zero for Sharpe
    sharpe = (ann_return - risk_free_rate) / ann_vol if ann_vol != 0 else 0
    
    # Max Drawdown calculation
    cum_rets = (1 + daily_returns).cumprod()
    max_drawdown = (cum_rets / cum_rets.cummax() - 1).min()
    
    return {
        "Total Return": total_return,
        "Annualized Return": ann_return,
        "Sharpe Ratio": sharpe,
        "Max Drawdown": max_drawdown
    }