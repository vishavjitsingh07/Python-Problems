def equation(i, j):
    x1, y1 = i 
    x2, y2 = j
    if x1 == x2: return float('inf'), x1
    m = round((y1 - y2) / (x1 - x2), 3)
    c = round(y1 - ((y1 - y2) / (x1 - x2))*x1, 3)
    return (m, c)

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2: return len(points)
        d = defaultdict(int)
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                x, y  = points[i], points[j]
                val = equation(x, y)
                d[val] +=1
        val = max(d.values())
        print(d)
        ans = int((1 + (1 + 8*val)**.5)//2)
        return ans
