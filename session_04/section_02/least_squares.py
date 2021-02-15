import csv
import math


def regression(file):
    i = 0
    a = 0.0
    b = 0.0

    sum_x = 0.0
    sum_y = 0.0
    sum_xy = 0.0
    sum_x2 = 0.0

    with open(file, 'r') as f:
        reader = csv.reader(f)
        next(reader)

        for line in reader:
            x = float(line[0])
            y = float(line[1])
            sum_x += x
            sum_y += y
            sum_xy += x * y
            sum_x2 += math.pow(x, 2)
            i += 1

        a = (i * sum_xy - sum_x * sum_y) / (i * sum_x2 - math.pow(sum_x, 2))
        b = (sum_x2 * sum_y - sum_xy * sum_x) / \
            (i * sum_x2 - math.pow(sum_x, 2))

        print(a)
        print(b)
    return


if __name__ == '__main__':
    regression('./data.csv')
