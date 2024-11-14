from statsmodels.tsa.arima.model import ARIMA

def arima(train, order=(2, 1, 2), n_forecast=20):
    
    model = ARIMA(train, order=order)
    fitted_model = model.fit()
    forecast = fitted_model.forecast(steps=n_forecast)

    return forecast