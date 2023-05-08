class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s, n = 0, len(mat)
        for i in range(n//2):
            s += sum([mat[i][i] ,mat[i][-1-i] ,mat[-1-i][i] ,mat[-1-i][-1-i]])
        return s if n%2==0 else s + mat[n//2][n//2]
