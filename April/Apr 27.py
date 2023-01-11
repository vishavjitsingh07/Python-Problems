class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        d = defaultdict(list)
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)

        def dfs(curr, par):
            time = 0
            for c in d[curr]:
                if c == par: continue
                cost = dfs(c, curr)
                if cost or hasApple[c]: time += cost + 2
            return time

        return dfs(0, -1)
