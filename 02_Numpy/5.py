import numpy as np

# Run-lenght encoding

def encode(data):
    elements = []
    repeat = []

    if len(data > 0):
        elements.append(data[0])
        repeat.append(1)
    
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            repeat[-1] += 1
        else:
            elements.append(data[i])
            repeat.append(1)

    elements = np.array(elements)
    repeat = np.array(repeat)
    return (elements, repeat)


# print(*encode(data))