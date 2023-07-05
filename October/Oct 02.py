class Solution:
    def stockBuyAndSell(self, n : int, prices) -> int:
        res = 0
        for i in range(n-1):
            res = res + (prices[i+1]-prices[i]) if prices[i]<prices[i+1] else res
        return res
        
