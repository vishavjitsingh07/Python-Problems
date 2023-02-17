class Solution():
    def solve(self, N, K, GeekNum):
        s = sum(GeekNum)
        currLen = K
        for i in range(N-K):
            GeekNum.append(s)
            currLen+=1
            s = s + GeekNum[-1] - GeekNum[currLen-K-1]
        return GeekNum[N-1]
