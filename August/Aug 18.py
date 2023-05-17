class Solution:
    def isPossible(self, n, m, s):
        dic={'L':0,'R':0,'U':0,'D':0}
        find={'L':'R','R':'L','U':'D','D':'U'}
        for el in s:
            dic[el]+=1
            if dic[find[el]]>0:
                dic[find[el]]-=1
            if dic['L']<0 or dic['R']<0 or dic['U']<0 or dic['D']<0:
                return 0
            if dic['L']>=m or dic['R']>=m or dic['U']>=n or dic['D']>=n:
                return 0
        return 1
