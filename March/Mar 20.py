class Solution:
    def rearrange(self,arr, n):
        val = []
        i = 0
        j = n-1
        while i<=j:
            val.append(arr[j])
            val.append(arr[i])
            i+=1
            j-=1
            
        for i in range(n):
            arr[i] = val[i]
