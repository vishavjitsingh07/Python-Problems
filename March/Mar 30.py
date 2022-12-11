class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        def dfs(root):
            if not root: return float('-inf')
            l, r = dfs(root.left), dfs(root.right)
            self.maxSum = max(root.val + l, root.val + r, root.val + l + r, self.maxSum, root.val, l, r)
            return max(root.val +l, root.val+r, root.val)
        dfs(root)
        return self.maxSum
