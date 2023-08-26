class Solution:
    def longestKSubstr(self, s, k):
        start, end, n, res, uniq, dp = 0, 0, len(s), -1, 0, [0]*26
        while end<=n:
            if uniq == k:
                res = max(res, end-start)
                if end<n and dp[ord(s[end]) - 97] != 0:
                    dp[ord(s[end]) -97] +=1
                    end+=1
                else:
                    while start<end and uniq == k:
                        dp[ord(s[start]) - 97] -=1
                        if dp[ord(s[start]) - 97] == 0: uniq -= 1
                        start+=1

            elif end<n and uniq < k:
                if dp[ord(s[end]) - 97] == 0: uniq +=1
                dp[ord(s[end]) - 97] +=1
                end+=1
                
            else: end+=1
            
        return res
