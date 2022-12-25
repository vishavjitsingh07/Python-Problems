import numpy as np
class Solution:
	def MissingNo(self, matrix):
        s = set()
        n = len(matrix)
        d1 = 0
        d2 = 0
        matrix = np.array(matrix)
        for i in range(n):
            if len(s)>2: return -1
            s.add(sum(matrix[i]))
            s.add(sum(matrix.T[i]))
        # print(s)
        if len(s)!=2: return -1
        ans = max(s) - min(s)
        
        for i in range(n):
            if matrix[i][i] == 0:
                matrix[i][i] = ans
            elif matrix[n-i-1][i] == 0:
                matrix[n-i-1][i] = ans
                
                
            d1 += matrix[i][i]
            d2 += matrix[n-i-1][i] 
            
        if d1 != d2 or d1!= max(s): return -1
        return ans
