class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        d = defaultdict(list)
        for i, j in edges:
            d[i].append(j)
            d[j].append(i)
        ans = [0]*n
        def dfs(curr, parr):
            curr_f = [0]*26
            for c in d[curr]:
                if c == parr: continue
                f = dfs(c, curr)
                for i in range(26):
                    curr_f[i] += f[i]
            curr_f[ord(labels[curr]) - ord('a')]+=1
            ans[curr] = curr_f[ord(labels[curr]) - ord('a')]
            return curr_f
        dfs(0, -1)
        return ans



