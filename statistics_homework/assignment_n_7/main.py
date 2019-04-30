import numpy as np

from general_tools.statistics import estimate_a, estimate_b, chi2
from general_tools.liniar_regression import estimate_coef, plot_regression_line, plot_residuals, plt


def plt_data(x, y):
    plt.plot(x, y, '*', label='data')


def q2():
    data = np.genfromtxt('stats_7_data.txt', delimiter='\t')[1:]

    x = np.array([i[1] for i in data])
    y = np.array([i[2] for i in data])

    # estimating coefficients
    b = estimate_coef(x, y)

    print("Estimated coefficients:\nb_0 = {}  nb_1 = {}".format(b[0], b[1]))
    # plotting regression line
    y_pred = plot_regression_line(x, y, b)

    print("var(y)=%s\nvar(y_pred)=%s" % (y.var(), y_pred.var()))
    rs = y_pred.var() / y.var()
    print("R^2=" + str(rs))

    plot_residuals(x, y, y_pred)


def plot_line(x, y, dy, func):
    y_pred = [func(xi) for xi in x]

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    plt.errorbar(x, y, yerr=dy, fmt="none", ecolor="r")
    plt_data(x, y)
    plt.savefig("line.png")

    # function to show plot
    plt.show()


def plot_residuals_lin(x, y, dy, func):
    y_pred = np.array([func(xi) for xi in x])
    y_diff = y - y_pred

    zero = [0 for _ in x]
    plt.plot(x, zero, color="b")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y - y_hat')

    plt.errorbar(x, y_diff, yerr=dy, fmt="none", ecolor="r")
    plt.savefig("line_ris.png")
    plt.show()


def q5():
    x = np.array([0, 1, 2, 3, 4, 5])
    y = np.array([0.92, 4.15, 9.78, 14.46, 17.26, 21.90])
    dy = np.array([0.5, 1.0, 0.75, 1.25, 1.0, 1.5])

    a = estimate_a(x, y, dy)
    b = estimate_b(x, y, dy, a)
    func = lambda x,: a * x + b
    chi_2 = chi2(x, y, dy, func)
    print(chi_2)
    plot_line(x, y, dy, func)
    plot_residuals_lin(x, y, dy, func)


if __name__ == '__main__':
    q2()
    q5()
