import numpy as np


def get_column(matrix, index):
    column = []
    for line in matrix:
        column.append(line[index])
    return column


def mult_lines(first, second):
    result = 0
    for i in range(len(first)):
        result += first[i] * second[i]
    return result


def no_numpy_mult(first, second):
    """
    param first: list of "size" lists, each contains "size" floats
    param second: list of "size" lists, each contains "size" floats
    """
    result = [[0 for i in range(len(first))] for i in range(len(first))]
    
    for i in range(len(first)):
        line = first[i]
        for j in range(len(second)):
            column = get_column(second, j)
            result[i][j] = mult_lines(line, column)
            
    return result        
            
    
    
        
    #YOUR CODE: please do not use numpy

    # result = []#YOUR CODE: create list of lists, not np.array
    return result

def numpy_mult(first, second):
    """
    param first: np.array[size, size]
    param second: np.array[size, size]
    """
    
    return first @ second


# first = np.array([[1, 2], [3, 4]])
# second = np.array([[5, 6], [8, 7]])
    