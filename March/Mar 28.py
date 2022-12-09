def numOfWays(M, N):
    ans = 0
    dirs = [(2, -1), (2, 1), (-2, 1), (-2, -1), (-1, 2), (1, 2), (1, -2), (-1, 2)]
    mod = 10**9 + 7
    def dfs(blackKnight):
        count = 1
        for i, j in dirs:
            l, m = blackKnight[0]+i, blackKnight[1]+j
            if 0<=l<M and 0<=m<N:
                count+=1
        return M*N - count
            
    for i in range(M):
        for j in range(N):
            ans += dfs((i, j))
    return ans%mod
