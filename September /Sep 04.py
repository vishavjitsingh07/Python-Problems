#User function Template for python3

class Solution:
    def reverseEqn( self,s):
        m,count=len(s)-1,0
        res=""
        while(m>=0): 
            if s[m] not in ["*","-","+","/"]:
                count+=1
            else:
                res+=(s[m+1:len(s)]+(s[m]))
                s=s[:m] 
                count=0 
            m-=1
        res+=s
        return res
