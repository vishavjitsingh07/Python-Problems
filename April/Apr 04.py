#User function Template for python3
from math import gcd
class Solution:    
    def maxGcd(self,N):
        r1,r2=N*(N-1),(N-1)*(N-2)
        k=N-2
        cnt=0
        while k>0:
            if gcd(r1,k)==1:
                r1*=k
                cnt+=1
            if cnt==2:
                break
            k-=1
        k=N-3
        cnt=0
        while k>0:
            if gcd(r2,k)==1:
                r2*=k
                cnt+=1
            if cnt==2:
                break
            k-=1
        return max(r1,r2)
        
        #code here
