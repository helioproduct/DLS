import numpy as np

data = np.array([1, 2, 2, 3, 3, 1, 1, 5, 5, 2, 3, 3])

mask = np.diff(data)

for i in range(len(mask)):
    if mask[i] != 0:
        mask[i] = 1

print(*data)
print(*np.diff(data))

# def encode(data):
#     print(*np.nonzero(np.diff(data)))
    

# encode(data)