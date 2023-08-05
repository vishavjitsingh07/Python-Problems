import sys
class Solution:
    def findMinDiff(self, arr,N,m):
        arr.sort()
        mindiff = sys.maxsize
        for i in range(len(arr)-m + 1):
            newMin = arr[i+m-1] - arr[i]
            if newMin < mindiff:
                mindiff = newMin
        return mindiff
