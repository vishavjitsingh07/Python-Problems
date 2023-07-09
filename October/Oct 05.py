#User function Template for python3

class Solution:
    def missingNumber(self,arr,n):
        s = set(arr)
        for i in range(1, len(s)+2):
            if i not in s: return i
                
                    
