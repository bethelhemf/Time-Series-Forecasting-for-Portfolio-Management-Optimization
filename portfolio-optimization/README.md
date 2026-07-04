# Prepare test data for LSTM
inputs = tsla_data[len(tsla_data) - len(test_data) - 60:].values
inputs = scaler.transform(inputs)
X_test, _ = create_sequences(inputs)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# LSTM Prediction
lstm_forecast = model.predict(X_test)
lstm_forecast = scaler.inverse_transform(lstm_forecast)

# Metrics Function
def evaluate(y_true, y_pred, name):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mape = mean_absolute_percentage_error(y_true, y_pred)
    return {"Model": name, "MAE": mae, "RMSE": rmse, "MAPE": mape}

results = [
    evaluate(test_data, arima_forecast, "ARIMA"),
    evaluate(test_data, lstm_forecast, "LSTM")
]
pd.DataFrame(results)