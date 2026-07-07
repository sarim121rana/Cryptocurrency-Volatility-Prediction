# Cryptocurrency-Volatility-Prediction
Project on Cryptocurrency Volatility Prediction using Machine Learning 
 
# 🪙 Cryptocurrency Volatility Prediction

An end-to-end Machine Learning web application designed to forecast cryptocurrency market volatility levels using historical price data and advanced technical indicators.
 

---

## 📊 Project Overview
Predicting market volatility is crucial for risk management and options trading strategies. This project engineering key technical features, trains a robust Machine Learning model (Decision Tree/Random Forest Regressor), and deploys it as an interactive dashboard.

### 🛠️ Tech Stack
* **Language:** Python
* **Machine Learning:** Scikit-Learn, Pandas, NumPy, Joblib
* **Web Interface:** Streamlit
* **Deployment & Cloud:** Hugging Face Spaces (Docker Environment)

### 📈 Input Features & Technical Indicators Used
The model utilizes the following engineered market features to make precise volatility forecasts:
* **Core Price Data:** Open, High, Low, Close, Volume, Market Cap, Liquidity Ratio
* **Trend Metrics:** Simple Moving Averages (`sma_7`, `sma_20`, `sma_21`)
* **Volatility Indicators:** Standard Deviation (`std_20`), Bollinger Bands (`bollinger_upper`, `bollinger_lower`), and Average True Range (`atr_14`)
