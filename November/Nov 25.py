# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        # code here
        total_sum = sum(arr)
        
        if total_sum % 2:
            return False
        
        target_sum = total_sum // 2
        
        dp = [1 if i == 0 else 0 for i in range(target_sum + 1)]
        
        for num in arr:
            achieved_sums = set()
            
            for j in range(num, target_sum + 1):
                if dp[j] == 0 and dp[j - num] and (j - num) not in achieved_sums:
                    dp[j] = 1
                    achieved_sums.add(j)
                if dp[target_sum]:
                    return 1
        
        return 0
