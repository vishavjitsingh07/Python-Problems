def fact(n):
    if n<= 1:
        return 1
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return int(factorial)

def combination(n, m): #4,2 
    return int((fact(n))/(fact(m)*fact(n-m)))


class Solution(object):
    def generate(self, numRows):
        pascalTriangle = []
        for i in range(numRows):
            arr = []
            for j in range(i+1):
                arr.append(combination(i, j))
            pascalTriangle.append(arr)
        return pascalTriangle
        
