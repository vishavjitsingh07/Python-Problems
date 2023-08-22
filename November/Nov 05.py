#User function Template for python3

class Solution:
    def findMinOpeartion(self, matrix, n):
        maxr=-1000000
        maxc=-1000000
        currsum=0
        for i in range(0,n,1):
            ans1=0
            ans2=0
            for j in range(0,n,1):
                ans1=ans1+matrix[i][j]
                ans2=ans2+matrix[j][i]
                currsum+=matrix[i][j]
            maxr=max(ans1,maxr)
            maxc=max(ans2,maxc)
        return max(maxr,maxc)*n-currsum
