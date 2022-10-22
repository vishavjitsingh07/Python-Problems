class Solution(object):
    def minWindow(self, s, t):
        lookUp = Counter(t)
        count = len(lookUp)
        mx = float('inf')
        n = len(s)
        start = 0
        end = 0
        output = ""
        while end<n:
            while end<n and count!=0:
                if s[end] in lookUp:
                    lookUp[s[end]] -=1
                    if lookUp[s[end]] == 0:
                        count-=1
                end+=1
            while start < end and count ==0:
                if end - start < mx:
                    mx = end-start
                    output = s[start:end]
                if s[start] in lookUp:
                    lookUp[s[start]] +=1
                    if lookUp[s[start]] >0:
                        count+=1
                start+=1
        return output
