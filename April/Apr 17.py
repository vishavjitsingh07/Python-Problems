class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        self.ans = 0
        startIdx, endIdx, empty = (0, 0), (0, 0), 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: startIdx = (i, j)
                elif grid[i][j] == 2:endIdx = (i, j)
                elif grid[i][j] == 0: empty +=1

        def dfs(node, visited, walk):
            if node == endIdx:
                if walk == empty+1: self.ans+=1
                return
            r, c = node
            if 0<=r<n and 0<=c<m and (r, c) not in visited and grid[r][c] !=-1:
                visited.add((r, c))
                for i, j in dirs:
                    dfs((r+i, c+j), visited, walk+1)
                visited.remove((r, c))

        dfs(startIdx, visited, 0)
        return self.ans
