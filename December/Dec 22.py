class Solution:
    def isBalanced(self,root):
    
        #add code here
        self.Bal = True
        
        def dfs(node):
            if node is None:
                return 0
            lft = dfs(node.left)
            rght = dfs(node.right)
            if abs(lft - rght) > 1:
                self.Bal = False
            return max(lft, rght) + 1
            
        dfs(root)
        return self.Bal


