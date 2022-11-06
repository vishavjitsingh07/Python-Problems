class Solution:
    def orderlyQueue(self, s, k):
        return min(s[i:] + s[:i] for i in range(len(s))) if k == 1 else "".join(sorted(s))
