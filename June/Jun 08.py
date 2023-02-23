class Solution:
    def uniquePaths(self, n, m, grid):
        
        mod = 1000000007
        paths = [[0]*m for i in range(n)]
        if grid[0][0] == 1:
            paths[0][0] = 1
        
        for i in range(1, n):
            if grid[i][0] == 1:
                paths[i][0] = paths[i-1][0]
                
        for j in range(1, m):
            if grid[0][j] == 1:
                paths[0][j] = paths[0][j-1]
                
        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] == 1:
                    paths[i][j] = (paths[i-1][j] + paths[i][j-1]) % mod
    
        return paths[-1][-1]
