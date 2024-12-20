import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def polynomial_regression(train, degree=2, n_forecast=20):
    """
    Perform polynomial regression on the given training data and forecast future values.
    
    Parameters:
        train (pd.Series or np.ndarray) : 
            The training data to fit the polynomial regression model.
        degree (int, optional) : 
            The degree of the polynomial features. Default is 2.
        n_forecast (int, optional) : 
            The number of future values to forecast. Default is 20.
    
    Returns:
        np.ndarray : 
            The forecasted values for the next n_forecast time steps.
    """
    
    x_train = np.arange(len(train)).reshape(-1, 1)
    y_train = train.values
    
    poly_features = PolynomialFeatures(degree=degree)
    x_poly = poly_features.fit_transform(x_train)
    
    model = LinearRegression()
    model.fit(x_poly, y_train)
    
    x_future = np.arange(len(train), len(train) + n_forecast).reshape(-1, 1)
    x_future_poly = poly_features.transform(x_future)
    predictions = model.predict(x_future_poly)
    
    return predictions