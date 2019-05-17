import numpy as np
import scipy as cp
import scipy.stats as sts


def calc_a(x, y):
    return np.cov(x, y)[0][1] / np.var(x)


def calc_b(y, x, a):
    return np.average(y) -a* np.average(x)

