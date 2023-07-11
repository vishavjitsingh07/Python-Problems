#User function Template for python3

class Solution:
    def findK(self, a, n, m, k):
        # Write Your Code here
        left =0
        right=m-1
        top=0
        bottom = n-1
        traversal=0
        count=0
        while left<=right and top<=bottom:
            if traversal==0:
                for i in range(left,right+1):
                    count+=1
                    if count==k:
                        return a[top][i]
                top+=1
                traversal=1
            elif traversal==1:
                for i in range(top,bottom+1):
                    count+=1
                    if count==k:
                        return a[i][right]
                right-=1
                traversal=2
            elif traversal == 2:  
                for i in range(right, left - 1, -1):
                    count+=1
                    if count==k:
                        return a[bottom][i]
                bottom -=1
                traversal= 3
            else: 
                for i in range(bottom, top - 1, -1):
                    count+=1
                    if count==k:
                        return a[i][left]
                left+=1
                traversal= 0
        
        return -1  
                    
