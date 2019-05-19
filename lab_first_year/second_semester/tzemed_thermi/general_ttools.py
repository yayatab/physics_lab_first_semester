from general_tools import round_to
from general_tools.lab import FitObject, n_sigma, calc_sigma_div
from lab_first_year.second_semester.electron_beam.general_tools import print_header
from scipy.stats import chi2

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


def get_new_vals(chisq, ndf, more_df=2):
    pval = 1 - chi2.cdf(chisq, ndf - more_df)
    chisq_red = chisq / (ndf - more_df)
    return chisq_red, pval


def third_fit(a1: FitObject, a2: FitObject, a3: FitObject, x: FitObject = default, y: FitObject = partical):
    theo = a1.val + a2.val * x.val + a3.val * x.val ** 2
    d1 = a1.err ** 2
    d2 = x.val * a2.err
    d3 = (a2.val + 2 * a3.val * x.val + 3 * a4.val * x.val ** 2) * x.err
    d4 = x.val ** 2 * a3.err
    d5 = x.val ** 3 * a4.err
    dtheo = calc_sigma_div(d1, d2, d3, d4, d5)
    print("theoretical:", theo, dtheo, dtheo / theo)
    print("messured:   ", y)
    return n_sigma(theo, dtheo, y.val, y.err)


if __name__ == '__main__':
    r = lambda x: round_to(x, 2)
    m = lambda fo: r(abs(fo.err / fo.val)) * 100
    print_header()
    a1 = FitObject("-11.73792 ± 0.1183326")
    a2 = FitObject("0.04254496 ± 0.0002598376")
    print(a1.val, '\t', r(a1.err), '\t', m(a1))
    print(a2.val, '\t', r(a2.err), '\t', m(a2))
    print(lin_fit(a1, a2))
    print(get_new_vals(4.001, 19, 0))
    print(get_new_vals(4.001, 19))
    print_header()
    a1 = FitObject("-9.766953 ± 0.5957537")
    a2 = FitObject("0.0332405 ± 0.009821332")
    a3 = FitObject("9.114287e-06 ± 4.430192e-06")
    print(a1.val, '\t', r(a1.err), '\t', m(a1))
    print(a2.val, '\t', r(a2.err), '\t', m(a2))
    print(a3.val, '\t', r(a3.err), '\t', m(a3))

    # a1 = FitObject("-9.776725 ± 1.758571")
    # a2 = FitObject("0.03325544 ± 0.02272265")
    # a3 = FitObject("9.2065e-06 ± 1.361191e-05")
    print(square_fit(a1, a2, a3))
    print(get_new_vals(19.392, 11, 0))
    print(get_new_vals(19.392, 11))
    print_header()
    a1 = FitObject("-9.459882 ± 0.2573542")
    a2 = FitObject("0.03104235 ± 0.003142925")
    a3 = FitObject("9.509518e-06 ± 6.62805e-07")
    a4 = FitObject("1.348157e-08 ± 3.383216e-09")
    print(a1.val, '\t', r(a1.err), '\t', m(a1))
    print(a2.val, '\t', r(a2.err), '\t', m(a2))
    print(a3.val, '\t', r(a3.err), '\t', m(a3))
    print(a4.val, '\t', r(a4.err), '\t', m(a4))

    print(third_fit(a1, a2, a3, a4))
    print(get_new_vals(25.482, 30, 0))
    print(get_new_vals(25.482, 30, 11))
