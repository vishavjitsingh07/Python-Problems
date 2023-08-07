class Solution:
    def isvalid(self,grid,row,col,val):
        for i in range(9):
            if grid[row][i]==val: return False
            if grid[i][col]==val: return False
            if grid[3*(row//3)+i//3][3*(col//3)+i%3]==val: return False
        return True
    def SolveSudoku(self,grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j]==0:
                    for c in range(1,10):
                        if self.isvalid(grid,i,j,c):
                            grid[i][j]=c
                            if self.SolveSudoku(grid):
                                return True
                            else:
                            
                                grid[i][j]=0
                    
                    return False
        
        return True
    def printGrid(self,arr):
        for i in range(9):
            for j in range(9):
                print(arr[i][j],end=" ")
