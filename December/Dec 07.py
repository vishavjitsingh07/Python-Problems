class Solution:
    def decodeAtIndex(self, S, K):   
        A = [1] # length of arrays: "leet2code3" -> [1,2,3,4,8,9,10,11,12,36]
        for x in S[1:]:
            # OPTIONAL: Early Stop (avoid repeating the string beyond the position "K")
            if A[-1] >= K : break
            #
            if x.isdigit():
                A.append( A[-1]*int(x) )
            else:
                A.append( A[-1]+1 )
        #
        for i in reversed(range(len(A))):
            K %= A[i]
            if not K and S[i].isalpha():
                return S[i]
