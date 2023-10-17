#User function Template for python3
class Solution:
    def transitiveClosure(self, N, graph):
        # code here
        for i in range(N): graph[i][i] = 1
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    graph[j][k] |= graph[j][i] & graph[i][k]
        
        return graph
