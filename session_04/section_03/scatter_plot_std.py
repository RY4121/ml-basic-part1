import numpy as np
import matplotlib.pyplot as plt


def standardize(x):
    x_mean = x.mean()
    std = x.std()

    return (x - x_mean) / std  # standarize


if __name__ == '__main__':
    data = np.loadtxt(fname='access.csv',
                      dtype='int',
                      delimiter=',',
                      skiprows=1
                      )
    x = data[:, 0]
    y = data[:, 1]

    standardized_x = standardize(x)

    plt.plot(standardized_x, y, 'o')
    plt.grid(True)
    plt.show()
