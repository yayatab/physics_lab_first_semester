from general_tools.lab import n_sigma, G_THEO, G_THEO_D, sqrt


def calc_mue(vi, vf, l, g=G_THEO):
    return (vi ** 2 - vf ** 2) / (2 * g * l)


def calc_mue_delta(vi, dvi, vf, dvf, l, dl, g=G_THEO, dg=G_THEO_D):
    d1 = (vi / (g * l)) * dvi
    d2 = (vf / (g * l)) * dvf
    d3 = ((vf ** 2 - vi ** 2) / (2 * l * g ** 2)) * dg
    d4 = ((vf ** 2 - vi ** 2) / (2 * g * l ** 2)) * dl
    return sqrt(sum([x ** 2 for x in [d1, d2, d3, d4]]))


def get_mue9_from_a1(a1, g=G_THEO):
    return -2 * a1 / g


def get_dmue9_from_da1(da1, g=G_THEO, dg=G_THEO_D):
    da1 = -2 / g  * da1
    dg = da1 / g ** 2 * dg
    return sqrt(da1 ** 2 + dg ** 2)
