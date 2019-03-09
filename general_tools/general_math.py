from math import factorial as factor


def root(x, n=2):
    return x ** (1 / n)


def n_over_k(n, k):
    return factor(n) / (factor(k) * factor(n - k))


def npr(n, k):
    return factor(n) / (factor(n - k))
