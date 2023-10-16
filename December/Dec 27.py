from typing import List

class Solution:
    def largestIsland(self, grid : List[List[int]]) -> int:
        n = len(grid)
        
        # Helper function for DFS to count island size
        def dfs(x, y, color):
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                grid[x][y] = color
                return 1 + dfs(x + 1, y, color) + dfs(x - 1, y, color) + dfs(x, y + 1, color) + dfs(x, y - 1, color)
            return 0
        
        color = 2  # Starting color for islands (0 and 1 are used for water and land)
        island_sizes = {0: 0}  # Dictionary to store island sizes, initialized with water size
        
        # Find island sizes and label them with unique colors
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i, j, color)
                    island_sizes[color] = size
                    color += 1
        
        max_size = max(island_sizes.values())
        
        # Iterate through 0's and try changing them to 1 and calculating the new size
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if 0 <= x < n and 0 <= y < n:
                            neighbors.add(grid[x][y])
                    max_size = max(max_size, sum(island_sizes[color] for color in neighbors) + 1)
        
        return max_size


