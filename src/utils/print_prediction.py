import matplotlib.pyplot as plt

def plot_results(train, test, predicted_values, title):
    plt.figure(figsize=(10, 5))
    plt.plot(range(len(train)), train, label='Train Data')
    plt.plot(range(len(train), len(train) + len(test)), test, label='Test Data')
    plt.plot(range(len(train), len(train) + len(test)), predicted_values, label='Predicted', linestyle='--')
    plt.title(title)
    plt.legend()
    plt.show()