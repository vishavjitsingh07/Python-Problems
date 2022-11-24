class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        m,n = len(board),len(board[0])
        
        def backtrack(i,j,k,visited):
            if board[i][j] == word[k]:
                if k==len(word)-1:
                    return True
                
                for xn,yn in directions:
                    x,y = i+xn,j+yn
                    if 0<=x<m and 0<=y<n and (x,y) not in visited:
                        if backtrack(x,y,k+1,visited.union({(x,y)}))==True:
                            return True
            
            return False
        
        for i in range(m):
            for j in range(n):
                if backtrack(i,j,0,{(i,j)}):
                    return True
        return False
