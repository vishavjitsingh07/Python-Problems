class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        if costs[0]> coins: return 0
        n = len(costs)
        for i in range(n):
            coins -=costs[i]
            if coins<0: return i 
        return n
