import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd


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
                            alpha=0.7, rwidth=0.5, bins='auto'):
    # An "interface" to matplotlib.axes.Axes.hist() method
    n, bins, patches = plt.hist(x=sequence, bins=bins, color=colour,
                                alpha=alpha, rwidth=rwidth, )
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.text(23, 45, r'$\mu=15, b=3$')
    # maxfreq = n.max()
    # Set a clean upper y-axis limit.
    # plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
    plt.savefig(file_path)

