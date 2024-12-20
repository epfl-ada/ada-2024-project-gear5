from statsmodels.tsa.arima.model import ARIMA

def arima(train, order=(2, 1, 2), n_forecast=20):
    """
    Fits an ARIMA model to the training data and generates a forecast.
    
    Parameters :
        train (array-like) : 
            The training data to fit the ARIMA model.
        order (tuple) : 
            The (p, d, q) order of the ARIMA model. Default is (2, 1, 2).
        n_forecast (int) : 
            The number of steps to forecast. Default is 20.
    Returns :
        array-like : 
            The forecasted values.
    """
    
    model = ARIMA(train, order=order)
    fitted_model = model.fit()
    forecast = fitted_model.forecast(steps=n_forecast)

    return forecast