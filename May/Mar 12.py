class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = defaultdict(list)
        for i, j, cost in flights:
            d[i].append((j, cost))
        
        q = deque()
        q.append((src, 0, k+1))
        ans = float("inf")
        visited  = set()
        Flag = False
        while q:
            currdst, currCost, k = q.popleft()
            if (currdst, currCost) in visited or k<0 or currCost> ans: continue
            visited.add((currdst, currCost))
            if currdst == dst:
                ans = min(ans, currCost)
                Flag = True
            for nextDst, newCost in d[currdst]:
                q.append((nextDst, currCost+newCost, k-1))
        return ans if Flag else -1

