#part 2 - riemann.py
import numpy as np
def left_endpoint(x_vals: np.ndarray, func: np.ufunc) -> float:
    #Make x_vals a sorted array
    x_vals = np.sort(x_vals)
    #Interval was given as [x_vals[0], x_vals[-1]]
    a, b = x_vals[0], x_vals[-1]
    #Find the width of each subinterval
    n = len(x_vals) - 1
    delta_x = (b - a) / n
    # Calculate left-endpoint sum
    left_sum = 0
    for i in range(n):
        left_sum += func(x_vals[i]) * delta_x
    return left_sum