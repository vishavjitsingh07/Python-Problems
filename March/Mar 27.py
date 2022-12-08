prime=[1]*(1000001)
primeArray=[]
def sieveOfEratosthenes(N):
    i=2
    while i*i<=N:
        if prime[i]:
            
            for j in range(i*i,N+1,i):
                prime[j]=0
        i+=1
    for i in range(2,N+1):
        if prime[i]:
            primeArray.append(i)
    
class Solution:
    def solve(self,n):
        counter=0
        index=0
        currNum=primeArray[index]*primeArray[index]
        while currNum<=n:
            counter+=1
            index+=1
            if index==len(primeArray):
                break
            currNum=primeArray[index]*primeArray[index]
        return counter
    def threeDivisors(self, query, q):
        sieveOfEratosthenes(1000000)
        ans=[]
        for el in query:
            ans.append(self.solve(el))
        return ans
