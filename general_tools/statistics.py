import numpy
import math
from general_tools import general_math


def mean_value(*args):
    """args = list of tuples(x, p(x)"""
    l = list(args)
    return sum([x * 1 / len(l) for x in l])


def expected_value(array):
    return numpy.mean(array)


def expected_value_weights(array, weights):
    return sum([x * y for x, y in zip(array, weights)])


def Binomial_distribution(n, p, r):
    return general_math.binomial_cooeficiant(n, r) * p ** r * (1 - p) ** (n - r)


def combination(n, k, *args):
    if len(args) % 2 != 0:
        print("please put even amount of numbers.")
    ret_val = general_math.n_over_k(n, k)
    l = list(args)
    for i in range(0, len(l), 2):
        print(l[i], l[i + 1])
        ret_val *= general_math.n_over_k(l[i], l[i + 1])
    return general_math.n_over_k(n, k)


def choosing_k_from_n(n, k):
    return combination(n, k)


def interchangeability(n, k):
    return general_math.binomial_cooeficiant(n, k)


def stirlings_approximation(n):
    return math.sqrt(2 * math.pi * n) * ((n / math.e) ** n)


def stirlings_approx_error(n):
    fact = general_math.factor(n)
    strling = stirlings_approximation(n)
    dx = abs(strling - fact) / fact
    return fact, strling, dx


def variance_for_Discrete(array, weights, mean_val):
    return sum([y * (x * mean_val) ** 2 for x, y in zip(array, weights)])


def variance_for_Discrete_with_squere(array, weights):
    e_squre = expected_value_weights([l ** 2 for l in array], weights)
    return e_squre - expected_value_weights(array, weights)


def geometrical_probability(n, p):
    return (1 - p ** (n - 1)) * p
