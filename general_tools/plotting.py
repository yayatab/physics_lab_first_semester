import matplotlib.pyplot as plt
import numpy as np

from general_tools import general_math


def _plot_grid(grid_kwargs):
    plt.grid(b=True, which='both', **grid_kwargs)
    plt.axhline(color='black')
    plt.axvline(color='black')


def _plot_several_lines(funcs, x):
    lines = []
    for func in funcs:
        yfunc = [func(i) for i in x]
        lines.append(yfunc)
    for y, func in zip(lines, funcs):
        plt.plot(x, y, label=func.__name__)


def plot_data(xdata, ydata):
    plt.plot(xdata, ydata, '*', label='data')


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
    _plot_several_lines(funcs, x)
    _plot_grid(grid_kwargs)
    plt.legend()
    plt.show()
    return plt


def plot_function_and_data(func, xdata, ydata, step: float = 0.1, grid_kwargs={}):
    plot_data(xdata, ydata)
    x = np.arange(min(xdata), max(xdata), step)
    if isinstance(func, list):
        _plot_several_lines(func, x)
    else:
        yfunc = [func(i) for i in x]
        plt.plot(x, yfunc, label=func.__name__)
    _plot_grid(grid_kwargs)
    plt.legend()
    plt.show()
    return plt


def plot_functions_and_data(funcs, xdata, ydata, step: float = 0.1, grid_kwargs={}):
    x = np.arange(min(xdata), max(xdata), step)
    _plot_several_lines(funcs, x)
    plot_data(xdata, ydata)
    _plot_grid(grid_kwargs)
    plt.legend()
    plt.show()
    return plt


if __name__ == '__main__':
    def x_squre(x):
        return x ** 2


    def x_third(x):
        return x ** 3


    plot_a_function(lambda x: general_math.exp(x), begin=-2, end=3, step=0.01,
                    grid_kwargs={'color': 'r', 'linestyle': '-', 'linewidth': 0.2})

    plot_functions([x_third, x_squre], begin=-0.9, end=0.9, step=0.01,
                   grid_kwargs={'color': 'r', 'linestyle': '-', 'linewidth': 0.2})

    x, y = [1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 20, 30, 40, 50, 60, 70, 80, 90]
    plot_function_and_data(x_third, x, y, step=0.01, grid_kwargs={'color': 'r', 'linestyle': '-', 'linewidth': 0.2})
    plot_functions_and_data([x_third, x_squre], x, y, step=0.01,
                            grid_kwargs={'color': 'r', 'linestyle': '-', 'linewidth': 0.2})
