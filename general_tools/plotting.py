import matplotlib.pyplot as plt
import numpy as np

from general_tools import general_math


def _plot_grid(grid_kwargs):
    plt.grid(b=True, which='both', **grid_kwargs)
    plt.axhline(color='black')
    plt.axvline(color='black')


def plot_a_function(func, begin: float = 0, end: float = 1e4, step: float = 0.1, grid_kwargs={}):
    return plot_functions([func], begin, end, step, grid_kwargs)


def plot_functions(funcs, begin: float = 0, end: float = 1e4, step: float = 0.1, grid_kwargs={}):
    """
    plots a function that take only one argument.

    :param func:
    :type func:
    :param begin:
    :type begin:
    :param end:
    :type end:
    :param step: density of line
    :type step:
    :param grid_kwargs: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.grid.html
    :type grid_kwargs: dict
    :return:
    :rtype:
    """
    x = np.arange(begin, end, step)
    lines = []
    for f in funcs:
        arr = []
        for i in x:
            arr.append(f(i))
        lines.append(arr)
    for y, func in zip(lines, funcs):
        plt.plot(x, y, label=func.__name__)
    _plot_grid(grid_kwargs)
    plt.legend()
    plt.show()
    return plt


if __name__ == '__main__':
    def x_squre(x):
        return x ** 2


    def x_third(x):
        return x ** 4


    plot_a_function(lambda x: general_math.exp(x), begin=-90, end=90, step=0.1,
                    grid_kwargs={'color': 'r', 'linestyle': '-', 'linewidth': 0.2})

    plot_functions([x_third, x_squre], begin=-0.9, end=0.9, step=0.01,
                   grid_kwargs={'color': 'r', 'linestyle': '-', 'linewidth': 0.2})
