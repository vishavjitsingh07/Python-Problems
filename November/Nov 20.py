from collections import deque
from typing import List

class Solution:
    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        if start == end:
            return 0
        
        queue = deque()
        MOD = 100000
        queue.append([start % MOD, 0])
        visited = set()
        visited.add(start)
        
        while queue:
            current_start, step = queue.popleft()
            if current_start == end:
                return step
            
            for x in arr:
                next_start = (current_start * x) % MOD
                if next_start not in visited:
                    queue.append([next_start, step + 1])
                    visited.add(next_start)
        
        return -1
