import matplotlib.pyplot as plt
import numpy as np


def plot_a_function(func, begin=0, end=1e4, step=0.1, grid_kwargs={}):
    """
    plots a function that take only one argument.

    :param func:
    :type func:
    :param begin:
    :type begin:
    :param end:
    :type end:
    :param step:
    :type step:
    :param grid_kwargs: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.grid.html
    :type grid_kwargs: dict
    :return:
    :rtype:
    """
    x = np.arange(begin, end, step)
    arr = []
    for i in x:
        arr.append(func(i))
    y = arr
    plt.plot(x, y)
    plt.grid(b=True, which='both', **grid_kwargs)
    plt.show()
    return plt


if __name__ == '__main__':
    plot_a_function(lambda x: x ** 3, begin=-9, end=9, step=0.01,
                    grid_kwargs={'color': 'r', 'linestyle': '-', 'linewidth': 0.2})
