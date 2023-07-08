#User function Template for python3

class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        if n<3:return 0
        arr.sort()
        for i in range(n-2):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            j=i+1
            k=n-1
            while(j<k):
                if(arr[i]+arr[j]+arr[k]==0):
                    return 1
                elif(arr[i]+arr[j]+arr[k] <0):
                    j+=1
                else:
                    k-=1
        return 0
