import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def differential(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


def function(x):
    return 0.01 * x ** 2 + 0.1 * x


def draw_line(f, x):
    diff = differential(f, x)
    print(diff)
    y = f(x) - diff * x
    return lambda n: diff * n + y


if __name__ == "__main__":
    x = np.arange(0.0, 20.0, 0.1)
    y = function(x)

    plt.xlabel("x")
    plt.ylabel("y")

    tf = draw_line(function, 10)
    y2 = tf(x)

    plt.plot(x, y)
    plt.plot(x, y2)
    plt.show()
