class Solution:
    def longestCycle(self, Edge: List[int]) -> int:      
        N = len(Edge)  
        d = defaultdict(list)
        for idx, i in enumerate(Edge):
            if i == -1: continue
            d[idx].append(i)
            
        self.ans = -1
        visited = dict()
        cycledRoot = set()
        def cycle(root):
            if root in cycledRoot: return
            cycledRoot.add(root)
            for i in d[root]:
                cycle(i)

        def dfs(root, visited, pos):
            if root in cycledRoot: return
            if root in visited:
                cycle(root)
                self.ans = max(max(visited.values()) - visited[root]+1, self.ans)
                return
            
            visited[root] = pos
            for i in d[root]:
                dfs(i, visited, pos+1)

        for i in range(N):
            visited = dict()
            dfs(i, visited, 0)
        return self.ans
