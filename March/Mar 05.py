class Solution:
	def totalWays(self, n, capacity):
	    capacity.sort()
	    ans ,mod = 1, 10**9 + 7
	    for i in range(n):
	        ans = ((capacity[i] - i)*ans)%mod
	    return ans% mod
