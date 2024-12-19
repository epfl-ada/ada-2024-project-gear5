import matplotlib.pyplot as plt

def plot_results(train, test, predicted_values, title):
    plt.figure(figsize=(10, 5))

    plt.plot(train.index, train, label='Train Data')
    plt.plot(test.index, test, label='Test Data')
    plt.plot(predicted_values.index, predicted_values, label='Predicted', linestyle='--')

    plt.title(title)
    plt.legend()
    plt.show()