from bisect import bisect_left
class Solution:
    def findMaxRow(self, mat, N):
        ans = 0
        row = -1
        for i in range(N):
            x = bisect_left(mat[i], 1)
            # print(x)
            if n-x>ans:
                ans = n-x
                row = i
        return (row, ans)
