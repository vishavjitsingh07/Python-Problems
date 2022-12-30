class Solution:
    def singlevalued(self, root):
        self.ans = 0
        
        def dfs(root):
            if root == None:
                return True
            left = dfs(root.left)
            right = dfs(root.right)
            if left and right:
                if root.left and root.left.data != root.data or root.right and root.right.data != root.data: return False
                else:
                    self.ans += 1
                    return True
                    
            return False
            
        dfs(root)
        return self.ans
