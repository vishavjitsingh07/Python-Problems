def subArr(i, j):
    n = j - i
    return ((n)*(n+1))//2
class Solution():
    def no_of_subarrays(self, n,arr):
        start = end = -1
        s = 0
        for i in arr:
            if i == 1:
                s += subArr(start, end)
                start = end = i
            else: end+=1
        return s + subArr(start, end)
