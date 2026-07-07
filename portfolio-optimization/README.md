# Time Series Forecasting for Portfolio Management Optimization

An end-to-end quantitative finance pipeline that integrates Deep Learning (LSTM) price forecasting with Modern Portfolio Theory (MPT) to construct and validate optimal investment portfolios.

## 🚀 Project Overview
This project demonstrates a production-grade workflow for financial analysis, moving from raw data acquisition to strategy backtesting. The core objective is to determine if AI-driven price forecasts can enhance portfolio risk-adjusted returns (Sharpe Ratio).

### Key Features:
- **Time Series Forecasting:** Comparative analysis using ARIMA (Statistical), Linear Regression (ML), and LSTM (Deep Learning).
- **Uncertainty Quantification:** Implementation of recursive multi-step forecasting with 95% confidence intervals (Fan Charts).
- **Portfolio Optimization:** Modern Portfolio Theory implementation using `PyPortfolioOpt` to find the Maximum Sharpe Ratio and Minimum Volatility portfolios.
- **Backtesting:** Validation of the optimized strategy against a passive 60/40 (SPY/BND) benchmark.

## 📁 Repository Structure
```text
portfolio-optimization/
├── data/               # Processed CSV files (TSLA, BND, SPY)
├── notebooks/          # Task-specific analysis (01 to 05)
├── src/                # Modular Python logic (Models, Optimizer, Backtester)
├── scripts/            # Global configuration (config.py)
├── requirements.txt    # Project dependencies
└── .gitignore          # Environment & cache exclusion