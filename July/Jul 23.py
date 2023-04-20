#User function Template for python3

class Solution:
    def smallestpositive(self, array, n): 
        # Your code goes here 
        miss=1
        array.sort()
        for i in range(n):
            if miss<array[i]:
                return miss
            else:
                miss+=array[i]
        return miss
