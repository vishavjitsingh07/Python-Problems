class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        d = defaultdict(list)
        for idx, i in enumerate(parent):
            if i !=-1 and s[i]!=s[idx]:
                d[i].append(idx)
                d[idx].append(i)

        n = len(s)
        visited = [False]*n
        self.dia = 1
        def dfs(curr, parr):
            visited[curr] = True
            currH = 1
            max1, max2 = 0, 0 #maintain 2 max length
            for c in d[curr]:
                if c == parr: continue
                currH = dfs(c, curr)
                if currH>max1: max2, max1 = max1, currH #update 2max with 1stmax and the max with new if new max found
                elif currH>max2: max2 = currH #Update the 2nd max with new Max if found 

            self.dia = max(self.dia, max1 + max2 + 1)
            return max(max1, max2) + 1

        for i in range(n):
            if visited[i] == False:
                dfs(i, -1)
        return self.dia



