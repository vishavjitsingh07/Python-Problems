class Solution:
    def isItPossible(sef, S, T, M, N):
        #code here
        st1 = st2 = ''
        for i,j in zip(S, T):
            if i!='#': st1+=i
            if j!="#": st2+=j
        return 1 if st1==st2 else 0
