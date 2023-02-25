#User function Template for python3

class Solution:
    def checkCompressed(self, S, T):
        n=""
        counter=0
        for i in range(len(T)):
            if T[i].isdigit():
                n+=T[i]
                counter-=1
            else:
                if n!="":
                    counter+=int(n)
                    n=""
                if T[i]!=S[counter]:
                    return 0
            counter+=1
        if n!="":
            counter+=int(n)
        if counter!=len(S):
            return 0
        return 1
                
