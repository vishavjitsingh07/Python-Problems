class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        def dfs(root):
            if not root: return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        dfs(root)
        ans = float('inf')
        for i in range(1, len(arr)):
            ans = min(arr[i] - arr[i-1], ans)
        return ans
