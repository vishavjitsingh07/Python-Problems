class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        def parser(edges):
            e = defaultdict(list)
            for u, v in edges:
                e[u].append(v)
            return e
        
        edges = [parser(redEdges), parser(blueEdges)]
        q = deque()
        INF = 10**9+8
        best = [[INF]*n for _ in range(2)]

        def enque(dis, node, color):
            q.append((dis, node, color))
            best[color][node] = dis

        for c in range(2):
            enque(0, 0, c)
        while q:
            dis, node, color = q.popleft()
            for v in edges[color][node]:
                newColor = 1 - color
                if best[newColor][v] == INF: enque(dis+1, v, newColor)
                
        ans = []
        for i in range(n):
            m = min(best[0][i], best[1][i])
            if m == INF: m = -1
            ans.append(m)
        return ans


        
        
