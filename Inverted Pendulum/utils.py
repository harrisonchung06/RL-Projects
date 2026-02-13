import numpy as np
import matplotlib.pyplot as plt

def plot(x_data,y_data, title, label_x, label_y):
    plt.plot(x_data, y_data)
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.title(title)
    plt.show()

def clamp(x, minimum, maximum):
    if x < minimum:
        return minimum
    if x > maximum:
        return maximum
    return x

def min_cap(x, min):
    if x < min:
        return min
    return x

def max_cap(x, max):
    if x > max:
        return max
    return x