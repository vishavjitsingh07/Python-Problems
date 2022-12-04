def minScore(n, roads):
        d = defaultdict(list)
        for i, j, x in roads:
            d[i].append((j, x))
            d[j].append((i, x))

        ans = [float('inf')]
        visit = set()
        def dfs(node):
            if not node in visit:
                visit.add(node)
                for nextNode, wt in d[node]:
                    ans[0] = min(ans[0], wt)
                    dfs(nextNode)
        dfs(1)
        return ans[0]
