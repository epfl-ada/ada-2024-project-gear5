import matplotlib.pyplot as plt

def plot_results(train, test, predicted_values, title):
    """Plot the results of a prediction.

    Parameters
    ----------
    train : list or array-like
        The training data.
    test : list or array-like
        The test data.
    predicted_values : list or array-like
        The predicted values.
    title : str
        The title of the plot.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(range(len(train)), train, label='Train Data')
    plt.plot(range(len(train), len(train) + len(test)), test, label='Test Data')
    prediction_range = range(len(train), len(train) + len(predicted_values))
    plt.plot(prediction_range, predicted_values, label='Predicted', linestyle='--')
    plt.title(title)
    plt.legend()
    plt.show()