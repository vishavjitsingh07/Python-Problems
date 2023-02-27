def isLeaf(self, grid):
        return all(grid[i][j] == grid[0][0] 
            for i in range(len(grid)) for j in range(len(grid[i])))
    def construct(self, grid):
        if not grid: return None
        size = len(grid)
        if self.isLeaf(grid): return Node(grid[0][0],True, None, None, None, None)
        
        tl = [[grid[row][col] for col in range(size//2) ]for row in range(size//2)]
        tr = [[grid[row][col] for col in range(size//2,size) ]for row in range(size//2)]
        bl = [[grid[row][col] for col in range(size//2) ]for row in range(size//2,size)]
        br = [[grid[row][col] for col in range(size//2,size) ]for row in range(size//2,size)]
        
        topLeft = self.construct(tl)
        topRight = self.construct(tr)
        bottomLeft = self.construct(bl)
        bottomRight = self.construct(br)
        value = topLeft.val or topRight.val or bottomLeft.val or bottomRight.val
        return Node(value,False,topLeft, topRight, bottomLeft, bottomRight)
