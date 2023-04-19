class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.mx = 0
        def dfs(node):
            if node is None: return (0, 0)
            left = dfs(node.left)[0] 
            right = dfs(node.right)[1]
            self.mx = max(self.mx, left, right)
            return (right + 1, left + 1)
        dfs(root)
        return self.mx
