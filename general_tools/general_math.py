from math import factorial as factor
from math import exp, sqrt, atan, atan2
import math


def root(x, n=2):
    return x ** (1 / n)


def n_over_k(n, k):
    return factor(n) / (factor(k) * factor(n - k))


def binomial_cooeficiant(n, k):
    return factor(n) / (factor(n - k))


def calc_asin_on_lists(A, B):
    return [math.asin(x / y) for x, y in zip(A, B)]
