#User function Template for python3

class Solution:
    def valid(self,i,j,n,m):
        if 0<=i<n and 0<=j<m:
            return True
        return False
    def hopscotch(self, n, m, mat, ty, i, j):
        # code here
        res=0
        if ty==0:
            if j%2:
                dir=[[-1,0],[1,0],[0,1],[1,-1],[1,1],[0,-1]]
                for nx,ny in dir:
                    if self.valid(i+nx,j+ny,n,m):res+=mat[i+nx][j+ny]
            else:
                dir=[[-1,0],[1,0],[0,1],[-1,1],[-1,-1],[0,-1]]
                for nx,ny in dir:
                    if self.valid(i+nx,j+ny,n,m):res+=mat[i+nx][j+ny]
        else:
            if j%2:
                dir=[[-1,-2],[-1,-1],[-2,0],[-1,1],[-1,2],[0,2],[1,2],[2,1],[2,0],[2,-1],[1,-2],[0,-2]]
                for nx,ny in dir:
                    if self.valid(i+nx,j+ny,n,m):res+=mat[i+nx][j+ny]
            else:
                dir=[[-2,-1],[-2,0],[-2,1],[-1,2],[0,2],[1,2],[1,1],[2,0],[1,-1],[1,-2],[0,-2],[-1,-2]]
                for nx,ny in dir:
                    if self.valid(i+nx,j+ny,n,m):res+=mat[i+nx][j+ny]
        return res
