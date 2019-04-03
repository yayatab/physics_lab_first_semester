from math import factorial as factor
from math import exp, sqrt, atan, atan2, log10, floor
import math


def root(x, n=2):
    return x ** (1 / n)


def n_over_k(n, k):
    return factor(n) / (factor(k) * factor(n - k))


def binomial_cooeficiant(n, k):
    return factor(n) / (factor(n - k))


def calc_asin_on_lists(A, B):
    return [math.asin(x / y) for x, y in zip(A, B)]


def round_to(x, d):
    """
    round a number to d digits.
    examples:
    in                     | out
    ------------------------------
    round_to_2(123.456, 0) | 100.0
    round_to_2(123.456, 1) | 120.0
    round_to_2(123.456, 6) | 123.456
    round_to_2(123.456, 5) | 123.456
    round_to_2(123.456, 4) | 123.46
    :param x: the number
    :param d: number of digits to round to
    :return: the rounded number
    """
    return round(x, d - int(floor(log10(abs(x)))))


def average_of_list(l: list) -> float:
    return sum(l) / len(l)
