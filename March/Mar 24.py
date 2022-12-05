from queue import Queue, deque
class Solution:
    def shotestPath(self, grid, n, m, k):
        queue = deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])
        if k > (len(grid) - 1 + len(grid[0]) - 1):
            return len(grid) - 1 + len(grid[0]) - 1
            
        while queue:
            x, y, k, c = queue.popleft()
            
            for dx, dy in [(x - 1, y), (x, y + 1),(x + 1, y), (x, y - 1)]:
                if dx == n - 1 and dy == m - 1:return c + 1
                if (0<=dx<n and 0<=dy<m) and (dx, dy, k - grid[dx][dy]) not in visited and (k - grid[dx][dy]) >=0:
                        visited.add((dx, dy, k-grid[dx][dy]))
                        queue.append((dx, dy, k-grid[dx][dy], c+1))
        return -1
