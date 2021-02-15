import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3
import numpy as np


def differential(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


def func(x1,
         x2,
         ):
    return x1**2 + x2**2


def function_1(x1):
    return x1**2 + 2.0**4.0


def function_2(x2):
    return x2**2 + 2.0**3.0


if __name__ == '__main__':
    # f(x1, x2) = x1 ^ 2+x2 ^ 2

    # partial differential
    print("x1 partial differential", differential(function_1, 3.0))
    print("x2 partial differential", differential(function_2, 4.0))

    # graph
    '''
    x1 = np.arange(-3, 3, 0.25)
    x2 = np.arange(-3, 3, 0.25)
    X1, X2 = np.meshgrid(x1, x2)
    Y = func(X1, X2)

    fig = plt.figure()
    ax = p3.Axes3D(fig)
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_zlabel("f(x1, x2)")
    ax.plot_wireframe(X1, X2, Y)
    plt.show()
    '''
