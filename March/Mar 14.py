class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s1 = set()
            s2 = set()
            for j in range(9):
                if board[i][j] in s1:
                    return False
                elif board[i][j] != ".":
                    s1.add(board[i][j])
                
                if board[j][i] in s2:
                    return False
                elif board[j][i] != ".":
                    s2.add(board[j][i])
        
        centre = [[1, 1], [4,1], [7,1], [1, 4], [4, 4], [7, 4], [1, 7], [4, 7], [7, 7]]
        dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]

        for i, j in centre:
            s = set()
            for diri, dirj in dir:
                ni = i + diri
                nj = j + dirj
                if board[ni][nj] in s:
                    return False
                elif board[ni][nj] != ".":
                    s.add(board[ni][nj])

        return True

