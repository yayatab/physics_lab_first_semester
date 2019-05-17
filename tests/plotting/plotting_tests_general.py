from general_tools import general_math
from general_tools.plotting import plot_a_function, plot_functions, plot_function_and_data, plot_functions_and_data

if __name__ == '__main__':
    def x_squre(x):
        return x ** 2


    def x_third(x):
        return x ** 3


    plot_a_function(lambda x: general_math.exp(x), begin=-2, end=3, step=0.01,
                    grid_kwargs={'color': 'r', 'linestyle': '-', 'linewidth': 0.2})

    plot_functions([x_third, x_squre], begin=-0.9, end=0.9, step=0.01,
                   grid_kwargs={'color': 'r', 'linestyle': '-', 'linewidth': 0.2})

    x, y = [1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 20, 30, 40, 50, 60, 70, 80, 90]
    plot_function_and_data(x_third, x, y, step=0.01, grid_kwargs={'color': 'r', 'linestyle': '-', 'linewidth': 0.2})
    plot_functions_and_data([x_third, x_squre], x, y, step=0.01,
                            grid_kwargs={'color': 'r', 'linestyle': '-', 'linewidth': 0.2})
