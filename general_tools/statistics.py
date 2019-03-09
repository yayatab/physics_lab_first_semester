from general_tools import general_math


def combination(n, k):
    return general_math.n_over_k(n, k)


def interchangeability(n, k):
    return general_math.npr(n, k)
