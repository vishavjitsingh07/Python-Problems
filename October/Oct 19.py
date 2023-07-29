

import sys
sys.setrecursionlimit(10**6)
class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        
        # Code here
        parent = {}
        def find(n, x):
            if not n:
                return None
            if n.left:
                parent[n.left] = n
            if n.right:
                parent[n.right] = n
            if n.data == x.data:
                return n
            elif n.data < x.data:
                return find(n.right, x)
            return find(n.left, x)
        n = find(root, x)
        
        if n.right:
            n = n.right
            while n and n.left:
                n = n.left
            return n

        while n:
            p = parent.get(n, None)
            if p and p.left == n:
                return p
            n = parent.get(n, None)
        return None
            
        
