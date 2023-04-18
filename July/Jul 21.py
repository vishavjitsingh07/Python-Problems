class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        n = min(len(word1), len(word2))
        for i in range(n):
            ans = ans + word1[i] + word2[i] 
        return ans + word1[n:] + word2[n:]
