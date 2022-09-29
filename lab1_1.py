import numpy as np

myA = np.array([
    [1, -5, -7, 1],
    [1, -3, -9, -4],
    [-2, 4, 2, 1],
    [-9, 9, 5, 3]])

myB = np.array([
    -75,
    -41,
    18,
    29
])

def Gauss_numpy_check(arr1, arr2):
    X = np.linalg.solve(arr1,arr2)
    for i in range(len(X)):
        print(f'x{i+1} = {round(X[i], 2)}')


Gauss_numpy_check(myA, myB)