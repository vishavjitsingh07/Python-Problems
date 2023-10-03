class Solution:
    def colName (self, n):
        ans = ""
        while n>=1: ans, n = (ans + chr(64 + n%26), n//26) if chr(64 + n%26) != '@' else (ans + 'Z', n//26 - 1)
        return ans[::-1]
