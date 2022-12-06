from queue import Queue, deque
def nearest1(grid, a, b, n, m):
    visit, q = set(), deque([(a, b, 0)])
    while q:
        x, y, count = q.popleft()
        visit.add((x, y))
        for i, j in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
            if 0<=i<n and 0<=j<m and (i, j) not in visit:
                if grid[i][j] == 1: return count+1
                q.append((i, j, count+1))
            
class Solution:
    def nearest(self, grid):
        n, m = len(grid), len(grid[0])
        ans = [[-1 for _ in range(m)] for __ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = 0 if grid[i][j] == 1 else nearest1(grid, i, j, n, m)
        return ans
