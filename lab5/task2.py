import numpy as np
def find_nearest(array, z):

    idx = np.abs(array - z).argmin()
    return array[idx]

array = np.random.rand(208,3)
print(array)

z = 0.2
print(find_nearest(array, z))