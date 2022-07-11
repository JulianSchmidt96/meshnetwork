import matplotlib.pyplot as plt
import numpy as np

def plot_cdf(data,x_label, figsize=(10,5), alpha=0.5):
    """
    _summary_
    Args:
        data ([dict]): dict of data to plot
        data.keys() : strings
        data[key]: np.array
        x_label (str): x label f.e. datarate etc..
        figsize (tuple): figure size
        alpha (float): transparency
    Returns:
        matplotlib.pyplot.figure: figure
    """

    plt.figure(figsize=figsize)
    plt.grid(alpha=alpha)

    for key in list(data.keys()):

        plot_data = data[key]
        plt.plot(np.sort(plot_data),
                np.linspace(0,1,len(plot_data)),
                label=key)

    plt.legend()
    plt.ylabel('occurence')
    plt.xlabel(x_label)
    plt.show()



def plot_metric(data,y_label, figsize=(10,5), alpha=0.5):
    """
    _summary_
    Args:
        data ([dict]): dict of data to plot
        data.keys() : strings
        data[key]: np.array
        y_label (str): y label f.e. datarate etc..
        figsize (tuple): figure size
        alpha (float): transparency
    Returns:
        matplotlib.pyplot.figure: figure
    """
    plt.figure(figsize=figsize)
    plt.grid(alpha=alpha)

    for i in range(len(list(data.keys()))):

        plot_data = data[list(data.keys())[i]]

        plt.bar(i, plot_data, label=list(data.keys())[i])
    plt.legend()
    plt.ylabel(y_label)
