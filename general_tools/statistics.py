import numpy
from general_tools import general_math


def mean_value(*args):
    """args = list of tuples(x, p(x)"""
    l = list(args)
    return sum([x * 1 / len(l) for x in l])


def expected_value(array):
    return numpy.mean(array)


def expected_value_weights(array, weights):
    return numpy.average(array, weights)


def Binomial_distribution(n, p, r):
    return general_math.binomial_cooeficiant(n, r) * p ** r * (1 - p) ** (n - r)


def combination(n, k):
    return general_math.n_over_k(n, k)


def interchangeability(n, k):
    return general_math.binomial_cooeficiant(n, k)
