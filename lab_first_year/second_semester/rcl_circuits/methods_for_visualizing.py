from general_tools.general_math import *
from general_tools.plotting import *

Rr = 6000
rt = 500 + Rr
L = 0.8261 * 1.5
C = 1.5e-9 * 0.91


def voltage_percentage_vs_phase(x, a1=L / rt, a2=rt * C, a3=Rr / rt):
    """ a1 = R_r
    a2 = R + tot
    a3 = L
    a4 = C
    """
    print(a1, a2, a3)
    derivitor = 1 + (a1 * x - 1 / (a2 * x)) ** 2
    return a3 / sqrt(derivitor)
    a11 = a1 * rt
    derivitor = rtot + (a1 * x - 1 / (a2 * x)) ** 2
    return a3 / sqrt(derivitor)


def f0(x):
    return voltage_percentage_vs_phase(x, a1=(L * 1.5) / rt, a2=rt * C * 0.91)


def f1(x):
    return voltage_percentage_vs_phase(x, a1=(L * 1.3) / rt, a2=rt * C * 0.91)


def f2(x):
    return voltage_percentage_vs_phase(x, a1=(L * 1.4) / rt, a2=rt * C * 0.91)


def f3(x):
    return voltage_percentage_vs_phase(x, a1=(L * 1.6) / rt, a2=rt * C * 0.91)


def f4(x):
    return voltage_percentage_vs_phase(x, a1=L / rt, a2=rt * C * 0.91)


def f5(x):
    return voltage_percentage_vs_phase(x, a1=(L * 1.2) / rt, a2=rt * C * 0.91)


def f6(x):
    return voltage_percentage_vs_phase(x, a1=(L * 1.1) / rt, a2=rt * C * 0.91)


def f41(x):
    return voltage_percentage_vs_phase(x, a1=L / rt, a2=rt * C * 1.51)


def f42(x):
    return voltage_percentage_vs_phase(x, a1=L / rt, a2=rt * C * 2)


def f43(x):
    return voltage_percentage_vs_phase(x, a1=L / rt, a2=rt * C)


def fit_funcs():
    return [f4, f42, f43]


def phase_as_function_of_omega(x, a1=L / rt, a2=rt * C):
    # \phi = arctan( (\omega*L - 1/\omega*C)/R)
    print(a1, a2)
    return atan(a1 * x - 1 / (a2 * x))


def f20(x):
    return phase_as_function_of_omega(x, a1=(L * 1.4) / rt, a2=rt * C * 0.91)


def f21(x):
    return phase_as_function_of_omega(x, a1=(L * 1.4) / rt, a2=rt * C * 0.91)


def f22(x):
    return phase_as_function_of_omega(x, a1=(L * 1.5) / rt, a2=rt * C * 0.99)


def f23(x):
    return phase_as_function_of_omega(x, a1=(L * 1.4) / rt, a2=rt * C * 0.81)


if __name__ == '__main__':
    # plot_a_function(voltage_percentage_vs_phase, begin=2701.769682, end=42914.15565, step=10)
    data = [2701.769682, 3330.088213, 5215.043805, 8984.954989, 10869.91058, 12754.86617, 14639.82177, 16524.77736,
            18409.73295, 20294.68854, 22179.64413, 24064.59973, 25949.55532, 27834.51091, 29719.4665, 31604.4221,
            33489.37769, 35374.33328, 37259.28887, 39144.24446, 41029.20006, 42914.15565, 22807.96267, 23122.12193,
            23436.2812, 26577.87385, 26892.03311, 27206.19238, 24504.4227, 24818.58196, 25132.74123, 25446.90049,
            24755.75011,
            ]

    datay = [0.041262136, 0.048543689, 0.065533981, 0.101941748, 0.132038835, 0.159223301, 0.19223301, 0.240776699,
             0.310679612, 0.422330097, 0.611650485, 0.854368932, 0.815533981, 0.54368932, 0.378640777, 0.276699029,
             0.218446602, 0.169902913, 0.13592233, 0.111650485, 0.085436893, 0.069417476, 0.694174757, 0.742718447,
             0.786407767, 0.718446602, 0.674757282, 0.631067961, 0.898058252, 0.90776699, 0.898058252, 0.873786408,
             0.912621359, ]
    # plot_data(data, datay)
    # plot_function_and_data(fit_funcs(), data, datay, step=10)
    #
    datax = [
        3330.088213, 5215.043805, 8984.954989, 10869.91058, 12754.86617, 14639.82177, 16524.77736,
        18409.73295, 20294.68854, 22179.64413, 24064.59973, 25949.55532, 27834.51091, 29719.4665, 31604.4221,
        33489.37769, 35374.33328, 37259.28887, 39144.24446, 41029.20006, 42914.15565, 22807.96267, 23122.12193,
        23436.2812, 26577.87385, 26892.03311, 27206.19238, 24504.4227, 24818.58196, 25132.74123, 25446.90049,
        24755.75011
    ]

    # # second part
    datay = [1.0296968008377505, 1.2870022175865687, 1.273199636441464, 1.2035883062370596, 1.2010870395684783,
             1.2413962034273813, 1.2246229304885385, 1.0694224805488273, 1.0361818409474326, 0.818554228802915,
             0.27622663076359155, 0.4561290225708227, 0.9582415884555576, 0.9623075646105371, 1.1036502157860613,
             1.0361818409474326, 1.2512151691232347, 1.2609516870532695, 1.2516224009967745, 1.1439029220222632,
             1.2231316863607218, 0.6751315329370317, 0.5769313452364567, 0.4956570772452796, 0.6881834620801937,
             0.7297276562269664, 0.792515024459304, 0.11985194670875002, 0.019682121802022043, 0.15276743158514852,
             0.30822817128795654, 0.005851097215445834
             ]

    for i in range(len(datax)):
        if datax[i] < 24800:
            datay[i] *= -1
    for i in datay:
        print(i)

    plot_function_and_data([phase_as_function_of_omega], datax, datay, step=10)
