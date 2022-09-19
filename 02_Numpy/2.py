import numpy as np

def no_numpy_scalar(v1, v2):
    return sum([v1[i] * v2[i] for i in range(3)])

def numpy_scalar (v1, v2):
    result = np.dot(v1, v2)    
    return result