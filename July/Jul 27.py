import heapq as heap
class Solution(object):
    def lastStoneWeight(self, stones):
        h = [-int(i) for i in stones]
        heapq.heapify(h)
        while len(h)>1:
            y = heap.heappop(h)
            x = heap.heappop(h)
            if x == y: continue
            heap.heappush(h, y-x)
            
        if not h: return 0
        else: return abs(heap.heappop(h))
