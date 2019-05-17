import numpy as np
import matplotlib.pyplot as plt
## Code for Question 1
# A planet in a circular orbit-simulation
from general_tools import plotting

if __name__ == '__main__':
    P = 5  # days
    K = 0.05  # km/s
    gamma = 30  # km/s
    epsilon = 0.01  # The uncertainty in velocity
    # (assuming a fixed uncertainty)
    # RV model
    t = np.random.uniform(0, 20, 20)

    RVfunc = lambda x: K * np.sin(2 * np.pi / P * x) + gamma + epsilon * np.random.normal()
    y = [RVfunc(x) for x in t]
    yerr = [1 for _ in y]
    xerr = [0 for _ in t]
    print(y, yerr)
    print(len(t), t, xerr)
    # plotting.plot_data([float(i) for i in t], [float(i) for i in y], xerr, yerr)
    # plt.show()

    plotting.plot_function_and_data(RVfunc, t, y, 0.1, yerr=yerr,xerr=xerr)
    #
    # vel = RVfunc(t)
    # evel = ones(size(t)) * epsilon
    # # Plot the simulated data, with the model
    # figure
    # plot(0: 0.01:20, K * sin(2 * pi / P * (0:0.01:20)) + gamma, ':k', 'linewidth', 2, 'color', [0.5, 0.5, 0.5]) hold
    # on
    # grid
    # on
    # errorbar(t, vel, evel, 'ok', 'markerfacecolor', 'r', 'markersize', 5)
    # xlabel('time [days]', 'fontsize', 14, 'interpreter', 'latex')
    # ylabel('RV [km/s]', 'fontsize', 14, 'interpreter', 'latex')
    # # Calculate the RV semiamplitude and ceter of mass velocity
    # # assuming that the orbital period is known.
    # # Setting the names of the variables for convinence:
    # x = sin(2 * pi / P * t)
    # y = vel
    # CovMat = cov(x, y)
    # K_hat = CovMat(2, 1) / CovMat(1, 1)
    # eK_hat = epsilon / (sqrt(length(t)) * std(x))
    # gam_hat = mean(y) - K_hat * mean(x)
    # egam_hat = epsilon / sqrt(length(t)) * (1 + mean(x) ^ 2 / var(x)) ^ (0.5)
    # plot(0: 0.01:20, K_hat * sin(2 * pi / P * (0:0.01:20)) + gam_hat, 'k') hold
    # on
    # grid
    # on
