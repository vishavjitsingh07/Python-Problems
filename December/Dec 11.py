class Solution:
    def BoundaryTraversal(self,matrix, n, m):
        arr = []
        if n == 1: return matrix[0]
        if m == 1: return [matrix[i][0] for i in range(n)]
        for i in range(0, m, 1)    : arr.append(matrix[0][i])
        for i in range(1, n-1, 1)  : arr.append(matrix[i][-1])
        for i in range(m-1, -1, -1): arr.append(matrix[-1][i])
        for i in range(n-2, 0, -1) : arr.append(matrix[i][0])
        return arr
