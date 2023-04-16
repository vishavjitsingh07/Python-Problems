from typing import List
class Solution:
    def solve(self, N : int, A : List[int], B : List[int]) -> int:
        sum_a=0
        sum_b=0
        aeo=[[],[]]
        beo=[[],[]]
        for i in range(N):
            sum_a+=A[i]
            sum_b+=B[i]
            if abs(A[i])%2==0:
                aeo[0].append(A[i])
            else:
                aeo[1].append(A[i])
            if abs(B[i])%2==0:
                beo[0].append(B[i])
            else:
                beo[1].append(B[i])
                
        if sum_a!=sum_b or len(aeo[0])!=len(beo[0]):
            return -1
        ans=0
        for i in range(2):
            aeo[i].sort()
            beo[i].sort()
            for j in range(len(aeo[i])):
                ans+=abs(aeo[i][j]-beo[i][j])//2
        return ans//2
        
