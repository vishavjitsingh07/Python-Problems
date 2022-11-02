def largestArea(n,m ,k, enemy):
        # code here
        rows = [0]
        col = [0]
        res = n*m
        for i in enemy:
            rows.append(i[0])
            col.append(i[1])
        rows.append(n+1)
        col.append(m+1)
        rows.sort()
        col.sort()
        maxR = 0
        maxC = 0
        for i in range(1, len(rows)):
            maxR = max(maxR, rows[i]-rows[i-1]-1)
        for i in range(1, len(col)):
            maxC = max(maxC, col[i]-col[i-1]-1)
        
        return maxR*maxC

