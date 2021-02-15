import numpy as np
import matplotlib.pyplot as plt


def standardize(x):
    x_mean = x.mean()
    std = x.std()

    return (x - x_mean) / std  # standarize


def f(standardized_x, param_0, param_1):
    return param_0 + param_1 * standardized_x


def objective_f(standardized_x, y, param_0, param_1):
    return 0.5 * np.sum(
        (
            y - f(standardized_x, param_0, param_1)
        ) ** 2
    )


def gradient_method(standardized_x, y):
    param_0 = np.random.rand()
    param_1 = np.random.rand()

    LNR = 1e-2

    difference = 1

    count = 0

    before = objective_f(standardized_x, y, param_0, param_1)

    while difference > 1e-2:
        tmp_param_0 = param_0 - LNR * np.sum(
            (
                f(standardized_x, param_0, param_1) - y
            )
        )
        tmp_param_1 = param_1 - LNR * np.sum(
            (
                f(standardized_x, param_0, param_1) - y
            ) * standardized_x
        )

        param_0 = tmp_param_0
        param_1 = tmp_param_1

        after = objective_f(standardized_x, y, param_0, param_1)
        difference = before - after
        before = after

        count += 1

        log = '({}) φ0: {:.3f} φ1: {:.3f} error: {:.4f}'
        print(log.format(count, param_0, param_1, difference))

    return param_0, param_1


if __name__ == "__main__":
    data = np.loadtxt(fname='access.csv',
                      dtype='int',
                      delimiter=',',
                      skiprows=1
                      )
    x = data[:, 0]
    y = data[:, 1]

    standardized_x = standardize(x)

    param_0, param_1 = gradient_method(standardized_x, y)

    x_axis = np.linspace(
        start=-3,
        stop=3,
        num=100
    )
    plt.plot(standardized_x, y, 'o')
    plt.plot(x_axis, f(x_axis, param_0, param_1))
    plt.grid(True)
    plt.show()
