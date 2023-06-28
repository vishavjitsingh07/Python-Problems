class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def maxDepth(self,root):
         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
    
