class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        def bfs(x):
            q = deque([x])
            color[x] = 1
            while q:
                cur = q.popleft()
                for n in graph[cur]:
                    if n not in color:
                        color[n] = -color[cur]
                        q += n,
                    elif color[n] == color[cur]:
                        return False
            return True
        
        return all(i in color or bfs(i) for i in range(len(graph)))
