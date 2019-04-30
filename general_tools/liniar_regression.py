import csv
import numpy as np
import matplotlib.pyplot as plt


def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)


def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m", marker="o", s=30)

    # predicted response vector
    y_pred = b[0] + b[1] * x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.savefig('figure.png')
    plt.show()

    return y_pred


def plot_residuals(x, y, y_pred):
    # plotting the actual points as scatter plot
    plt.scatter(x, (y_pred - y), color="m",
                marker="o", s=30)

    zero = [0 for xi in x]
    plt.plot(x, zero, color="b")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('e')

    plt.savefig('risiduals.png')

    # function to show plot
    plt.show()

