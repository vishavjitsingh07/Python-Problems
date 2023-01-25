class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)
        def pall(idx, curr):
            if idx == n: 
                ans.append(curr)
                return
            for i in range(idx, n):
                if s[idx:i+1] == s[idx:i+1][::-1]:
                    pall(i+1, curr + [s[idx:i+1]])

        pall(0, [])
        return ans
