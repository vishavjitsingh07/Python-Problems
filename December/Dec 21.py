class Solution:
    
    def KDistanceNodes(self,root,target,k):
        ans=[]
        lft=[]
        rgt=[]
        def find(root,target,k,i):
            if root:
                if root.data==target:
                    ans.append(root)
                    return 1
                a=find(root.left,target,k,i+1)
                if a:
                    rgt.append([root,a])
                    return a+1
                b=find(root.right,target,k,i+1)
                if b:
                    lft.append([root,b])
                    return b+1
            return
        find(root,target,k,10000000)
        
        r_ans=[]

        def find(root,k):
            if root:
                if k==0:
                    r_ans.append([root.data,root])
                    return
        
                find(root.left,k-1)
                find(root.right,k-1)
            return
        
        for el in ans:
            find(el,k)
            
        for el in lft:
            if (k-el[1])==0:
                r_ans.append([el[0].data,el])
            elif k-el[1]>0:
                find(el[0].left,k-el[1]-1)

        for el in rgt:
            if (k-el[1])==0:
                r_ans.append([el[0].data,el])
            elif k-el[1]>0:
                find(el[0].right,k-el[1]-1)
        
        r_ans.sort(key=lambda x:x[0])
        
        ans=[]
        for el in r_ans:
            ans.append(el[0])
        return ans

