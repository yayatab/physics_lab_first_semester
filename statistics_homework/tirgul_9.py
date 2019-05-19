import numpy as np

if __name__ == '__main__':
    P = 5;  # days
    K = 0.05;  # km/s
    gamma = 30;  # km/s
    epsilon = 0.01;

    RVfunc = lambda x: K * np.sin(2 * np.pi / P * x) + gamma + epsilon * np.random.normal(x)
    t = np.random.uniform(0, 20, 20)
    vel = K * np.sin(2 * np.pi / P * t) + gamma + epsilon * np.random.normal(t)
    print(t)
    ## Second part: code for Question 4
    # Define the Design matrix:
    x0 = np.ones((1, 20))
    x1 = np.sin(2 * np.pi / P * t)
    x2 = np.cos(2 * np.pi / P * t)
    M = [x0, x1, x2]
    # Define the error matrix:
    C1 = np.diag(np.ones((1, 20)), k=int(epsilon))
    # Define velocity vector:
    y = vel[:]
    # Solve for theta:
    MT = np.conj(M).transpose()
    print("@" * 80)
    print("@" * 80)
    print("@" * 80)
    print(M)
    print("@" * 80)
    print("@" * 80)
    print("@" * 80)
    print("@" * 80)
    print("@" * 80)
    print("@" * 80)
    print(MT)
    m = MT @ C1 @ M
    hui = MT @ C1 @ y
    theta = np.invert(m) * hui
    print(theta)



