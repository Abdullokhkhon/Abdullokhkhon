myA = [
    [15,8,0,0,0],
    [2,-15,4,0,0],
    [0,4,11,5,0],
    [0,0,-3,16,-7],
    [0,0,0,3,8]
    ]

myB = [
    92,
    -84,
    -77,
    15,
    -11
    ]

def Output( text, name, var ):
    if (type(var) == int) or (type(var) == float):
        print(var)
    else:
        print( text )
        for k in range(len(var)):   
            print(f"{name}[{k}] = {var[k]:6.2f}")


def Array_chek(a):
    n = len(a)
    
    for i in range(0, n):
        if( len(a[i]) != n ):
            print('Размерность не соответствует')
            return False
    
    for i in range(1, n - 1):
        if(abs(a[i][i]) < abs(a[i][i - 1]) + abs(a[i][i + 1])):
            print('Условие достаточности не выполнено')
            return False

    if (abs(a[0][0]) < abs(a[0][1]))or(abs(a[n - 1][n - 1]) < abs(a[n - 1][n - 2])):
        print('Условие достаточности не выполнено')
        return False
    
    
    for i in range(0, len(a)):
        if( a[i][i] == 0 ):
            print('На главной диагонали есть нулевые значения')
            return False
    return True


def solution(arr1, arr2):
    if( not Arrey_chek(arr1) ):
        print('Ошибка в вводных данных')
        return -1 

    n = len(arr1)
    x = [0 for i in range(0, n)]
    print('Размерность матрицы: ',n,'x',n)
    
    v = [0 for i in range(0, n)]
    u = [0 for i in range(0, n)]

    v[0] = arr1[0][1] / (-arr1[0][0]) 
    u[0] = ( - arr2[0]) / (-arr1[0][0]) 
    for i in range(1, n - 1): 
        v[i] = arr1[i][i+1] / ( -arr1[i][i] - arr1[i][i-1]*v[i-1] )
        u[i] = ( arr1[i][i-1]*u[i-1] - arr2[i] ) / ( -arr1[i][i] - arr1[i][i-1]*v[i-1] )
    v[n-1] = 0
    u[n-1] = (arr1[n-1][n-2]*u[n-2] - arr2[n-1]) / (-arr1[n-1][n-1] - arr1[n-1][n-2]*v[n-2])
    
    Output('Коэффициенты V: ','V', v)
    Output('Коэффициенты U: ','U', u)
    
    x[n-1] = u[n-1]
    for i in range(n-1, 0, -1):
        x[i-1] = v[i-1] * x[i] + u[i-1]
    return x    


x = solution(myA, myB)
Output('Решение: ','x', x)