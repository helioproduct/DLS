import numpy as np

def cumsum(A):
    result = np.empty(A.shape)
    for i in range(len(A)):
        new_line = np.cumsum(A[i])
        result[i] = new_line    
    return result