class Solution:
    def helpp(self,root,dic):
        if not root:
            return ""
        s=self.helpp(root.left,dic)+str(root.data)+self.helpp(root.right,dic)
        if s not in dic: dic[s]=1
        else: dic[s]+=1
        return s
    def dupSub(self, root):
        dic={}
        s=self.helpp(root,dic)
        for i ,j in dic.items():
            if len(i) >= 2 and j>1:
                return 1
        return 0
