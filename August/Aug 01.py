class Solution:
    def powerfullInteger(self,n,intervals,k):
        d={}
        for start,end in intervals:
            if start not in d:
                d[start]=0
            if end+1 not in d:
                d[end+1]=0
            d[start]+=1
            d[end+1]-=1
        v=-1
        temp=0
        for el in sorted(d.keys()):
            if d[el]>=0:
                    
                temp+=d[el]
                if temp>=k:
                    v=el
            else :
                if temp>=k:
                    v=el-1
                temp+=d[el]
        return v
