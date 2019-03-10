import numpy


def mean_value(*args):
    """args = list of tuples(x, p(x)"""
    l = list(args)
    return sum([x * 1 / len(l) for x in l])


def expected_value(array):
    return numpy.mean(array)


def expected_value_weights(array, weights):
    return numpy.average(array, weights)


def Binomial_distribution(n, p, r):
    # TODO use mathematis.
    # ToDO call npr as Binomial coefficient.
    return mathematis.npr(n, r) * p ** r * (1 - p) ** (n - r)
