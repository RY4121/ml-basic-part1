import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname='access.csv',
                  dtype='int',
                  delimiter=',',
                  skiprows=1
                  )
x = data[:, 0]
y = data[:, 1]

plt.plot(x, y, 'o')
plt.grid(True)
plt.show()
