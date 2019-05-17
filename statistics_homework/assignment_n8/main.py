import numpy as np
import general_tools.histogram

from general_tools.statistics.linear_fit import calc_a, calc_b

X_LENGTH = 50
N = 10000


def generate_rnd_x_and_eps():
    return np.random.uniform(low=-3.0, high=7.0, size=X_LENGTH), np.random.normal(size=X_LENGTH)


def func(x, epsilon_i, a=1.2, b=5):
    return a * x + b + epsilon_i


def print_avg_and_var(z, zs):
    print("avarage,variance of " + z, np.average(zs), np.var(zs))


if __name__ == '__main__':
    a_hats = []
    b_hats = []
    for i in range(N):
        x, epsilon = generate_rnd_x_and_eps()
        y = []
        for xi, ei in zip(x, epsilon):
            y.append(func(xi, ei))
        a_hats.append(calc_a(x, y))
        b_hats.append(calc_b(x, y, a_hats[-1]))
    general_tools.generate_histogram_auto(a_hats, file_path="./a_hats")
    general_tools.generate_histogram_auto(b_hats, file_path="./b_hats")
    print_avg_and_var("a", a_hats)
    print_avg_and_var("b", b_hats)
    """
    we anticipate that the avg of a will be 1.2 +-
    we anticipate that the avg of v will be 1.2 -7
    """
