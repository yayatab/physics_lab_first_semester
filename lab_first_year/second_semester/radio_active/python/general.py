from math import sqrt

from general_tools.lab import FitObject
from lab_first_year.second_semester.electron_beam.general_tools import print_header


def a():
    a1 = FitObject("13.86049 ± 0.1732939")
    a2 = FitObject("0.000850132 ± 0.0008038052")
    """
    chi^2_reduced = 0.9905
    p probability = 0.47119
    """
    mu = 13.79454545
    sigma = 4.006763291
    l = FitObject(mu, sigma / sqrt(550))
    lt = FitObject(sigma ** 2, 2 * sigma ** 2 / sqrt(2 * 550 - 2))
    print("fit objects", '\n\t', a1, '\n\t', a2)
    print("lambdas, orig an tag", '\n\t', l, '\n\t', lt)
    print(l.calc_n_sigma(a1))
    print(lt.calc_n_sigma(a1))


def b():
    a1 = FitObject("3.533558 ± 2.977524")
    a2 = FitObject("0.1668381 ± 0.1557471")
    a3 = FitObject("0.1766915 ± 0.2236136")

    """
    chi^2_reduced = 0.95561
    p probability = 0.45368 
    """
    print("fit objects", '\n\t', a1, '\n\t', a2, '\n\t', a3)

def c():


if __name__ == '__main__':
    a()
    print_header()
    b()
    print_header()
    c()
