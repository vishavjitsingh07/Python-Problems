class Solution:
    def klengthpref(self,arr,n,k,s):
        return 0 if k>len(s) else sum(1 for i in arr if i[:k] == s[:k])
