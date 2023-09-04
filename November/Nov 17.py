class Solution:
    def fill(self, n, m, mat):
        visited = set()
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def dfs(mat, i, j):
            if (i, j) in visited: 
                return
            
            visited.add((i, j))
            for x, y in dir:
                if (0<= i + x < n) and (0 <= j+y < m) and mat[i + x][j + y] == "O":
                    dfs(mat, i+x, j+y)
            return
        
        for i in range(n):
            for j in range(m):
                if (i==0 or j == 0 or i == n-1 or j==m-1) and mat[i][j] == "O":
                    dfs(mat, i, j)
                    
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited:
                    mat[i][j] = "X"
        return mat
