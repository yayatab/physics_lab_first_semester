import matplotlib.pyplot as plt
from collections import Counter
import numpy as np


def create_histogram(sequence) -> dict:
    hist = {}
    for i in sequence:
        hist[i] = hist.get(i, 0) + 1
    return hist


def histogram_with_counter(seq) -> Counter:
    return Counter(seq)


def ascii_histogram(seq) -> None:
    """A horizontal frequency-table/histogram plot."""
    counted = create_histogram(seq)
    for k in sorted(counted):
        print('{0:5d} {1}'.format(k, '+' * counted[k]))


def generate_histogram_auto(sequence, file_path='./figure.jpeg', xlabel="", ylabel="", title="", colour='#0504aa',
                            alpha=0.7, rwidth=0.5, bins='auto', normalize=False, plot_args={}):
    # An "interface" to matplotlib.axes.Axes.hist() method
    n, bins, patches = plt.hist(x=sequence, bins=bins, color=colour, alpha=alpha, rwidth=rwidth, )
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    # Set a clean upper y-axis limit.
    if normalize:
        maxfreq = n.max()
        plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
    plt.savefig(file_path)
    plt.plot(**plot_args)
    plt.show()


if __name__ == '__main__':
    from random import random
    generate_histogram_auto([random() for i in range(1000)], bins=30)
