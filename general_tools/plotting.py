import matplotlib.pyplot as plt
import numpy as np


def plot_a_function(func, begin=0, end=1e4, step=0.1):
    x = np.arange(begin, end, step)
    arr = []
    for i in x:
        arr.append(func(i))
    y = arr
    plt.plot(x, y)
    plt.show()
