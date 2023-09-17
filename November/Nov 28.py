class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        def test(node):
            q, seen, depth = deque([(node, 1<<node)]), {(node, 1<<node)}, 0
            while q:
                c = len(q)
                for _ in range(c):
                    node, path = q.pop()
                    if path == (1<<n)-1: return depth
                    for nei in graph[node]:
                        if (nei, path|(1<<nei)) in seen: continue
                        seen.add((nei, path|(1<<nei)))
                        q.appendleft((nei, path|(1<<nei)))
                depth+=1
            return -1
        return [min(x) if x else n-1 for x in [[test(node) for node in range(n) if len(graph[node]) == 1]]][0]
