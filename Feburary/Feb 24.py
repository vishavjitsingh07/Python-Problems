class Solution:
    def removals(self,arr, n, k):
        arr.sort()
        
        l,r = 0,0
        ans = 0
        while l<n and r<n:
            if arr[r]-arr[l]<= k: r += 1
            else:
                count = max(r-l+1, ans)
                l += 1
                
        ans = max(r-l+1, ans)
        return n-ans+1
