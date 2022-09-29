myA=[
    [1, -5, -7, 1],
    [1, -3, -9, -4],
    [-2, 4, 2, 1],
    [-9, 9, 5, 3]
]
myB = [
    -75,
    -41,
    18,
    29
]

def Output(arr1, arr2):
    for row in range(len(arr1)):
        print('(', end='')
        for col in range(len(arr1[0])):
            print(f'{arr1[row][col]:8.2f}', end=' ')
        print(f') * (x{row+1:8.2f}) = ({arr2[row]:8.2f})')
    print('-'*35)


def RowDivide(arr1, arr2, row, divider):
    arr1[row] = [a / divider for a in arr1[row]]
    arr2[row] /= divider


def RowSum(arr1, arr2, row, source_row, coefficient):
    arr1[row] = [(a + k * coefficient) for a, k in zip(arr1[row], arr1[source_row])]
    arr2[row] += arr2[source_row] * coefficient


def Gauss(arr1, arr2):
    column = 0
    while column < len(arr2):
        RowDivide(arr1, arr2, column, arr1[column][column])
        Output(arr1, arr2)
        for i in range(len(arr1) - 1 - column):
            RowSum(arr1, arr2, i+1+column, column, -arr1[i + 1 + column][column])
        Output(arr1, arr2)
        column += 1
    X = [0 for b in arr2]
    for i in range(len(arr2)-1, -1, -1):
        X[i] = arr2[i] - sum(x * a for x, a in zip(X[(i + 1):], arr1[i][(i + 1):]))
    for i in range(len(X)):
        print(f'x{i+1} = {round(X[i], 2)}')


Gauss(myA, myB)