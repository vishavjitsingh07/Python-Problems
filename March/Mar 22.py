class Solution:
    def helper(self, stalls, gap, cows):
        prev, cows = stalls[0], cows-1
        
        for i in stalls:
            if i-prev >= gap:
                cows, prev = cows-1, i
                if not cows: return True
                #if cows==0: return True
        return False
    
    def solve(self, n, k, stalls):
        start, end, ans = 1, 10**9, -1
        stalls.sort()
        
        while start<=end:
            mid = start + (end-start)//2
            if self.helper(stalls, mid, k): start, ans = mid+1, mid
            else: end = mid-1
        return ans
