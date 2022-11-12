
class Solution:
    def characterReplacement(self, s, k):
        # Code here
        max_freq=0
        m={}
        ans=0
        j=0
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]]=1
            else:
                m[s[i]]+=1
            max_freq=max(max_freq,m[s[i]])
            while(i-j+1-max_freq>k):
                m[s[j]]-=1
                j+=1
            ans=max(ans,i-j+1)
        return ans
