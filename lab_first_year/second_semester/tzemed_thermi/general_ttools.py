from general_tools.lab import FitObject, n_sigma, calc_sigma_div
from lab_first_year.second_semester.electron_beam.general_tools import print_header

T0 = FitObject(2.047348, 0.267286363)
default = FitObject(-187.946 + 273.15 - T0.val, 0.267286363)
partical = FitObject(-5.8, 0.01826)


def lin_fit(a1: FitObject, a2: FitObject, x: FitObject = default, y: FitObject = partical):
    theo = a1.val + a2.val * x.val
    d1 = a1.err ** 2
    d2 = x.val * a2.err
    d3 = x.err * a2.val
    dtheo = calc_sigma_div(d1, d2, d3)
    print("theoretical:", theo, dtheo, dtheo / theo)
    print("messured:   ", y)
    return n_sigma(theo, dtheo, y.val, y.err)


def square_fit(a1: FitObject, a2: FitObject, a3: FitObject, x: FitObject = default, y: FitObject = partical):
    theo = a1.val + a2.val * x.val + a3.val * x.val ** 2
    d1 = a1.err ** 2
    d2 = x.val * a2.err
    d3 = (a2.val + 2 * a3.val * x.val) * x.err
    d4 = x.val ** 2 * a3.err
    dtheo = calc_sigma_div(d1, d2, d3, d4)
    print("theoretical:", theo, dtheo, dtheo / theo)
    print("messured:   ", y)
    return n_sigma(theo, dtheo, y.val, y.err)


def third_fit(a1: FitObject, a2: FitObject, a3: FitObject, x: FitObject = default, y: FitObject = partical):
    theo = a1.val + a2.val * x.val + a3.val * x.val ** 2
    d1 = a1.err ** 2
    d2 = x.val * a2.err
    d3 = (a2.val + 2 * a3.val * x.val+3*a4.val*x.val**2) * x.err
    d4 = x.val ** 2 * a3.err
    d5 = x.val**3 * a4.err
    dtheo = calc_sigma_div(d1, d2, d3, d4,d5)
    print("theoretical:", theo, dtheo, dtheo / theo)
    print("messured:   ", y)
    return n_sigma(theo, dtheo, y.val, y.err)


if __name__ == '__main__':
    print_header()
    a1 = FitObject("-11.73792 ± 0.1183326")
    a2 = FitObject("0.04254496 ± 0.0002598376")
    print(lin_fit(a1, a2))
    print_header()
    # a1 = FitObject("-6.696857 ± 1.11334")
    # a2 = FitObject("0.03768008 ± 0.4735286")
    # a3 = FitObject("9.999818e-09 ± 9.700954e-06")
    a1 = FitObject("-9.766953 ± 0.5957537")
    a2 = FitObject("0.0332405 ± 0.009821332")
    a3 = FitObject("9.114287e-06 ± 4.430192e-06")

    # a1 = FitObject("-9.776725 ± 1.758571")
    # a2 = FitObject("0.03325544 ± 0.02272265")
    # a3 = FitObject("9.2065e-06 ± 1.361191e-05")
    print(square_fit(a1, a2, a3))
    print_header()
    a1 = FitObject("-9.459882 ± 0.2573542")
    a2 = FitObject("0.03104235 ± 0.003142925")
    a3 = FitObject("9.509518e-06 ± 6.62805e-07")
    a4 = FitObject("1.348157e-08 ± 3.383216e-09")

    print(third_fit(a1, a2, a3, a4))
