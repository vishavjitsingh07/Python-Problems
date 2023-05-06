
#Back-end complete function Template for Python 3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def goodSubtrees(self,root,k):
        ans=0
        def solve(root):
            nonlocal ans
            if not root:
                return set()
            temp=set()
            temp.add(root.data)
            temp|=solve(root.left)
            temp|=solve(root.right)
            if len(temp)<=k:
                ans+=1
            return temp
        solve(root)
        return ans

