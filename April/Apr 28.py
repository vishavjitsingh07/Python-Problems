class Solution:
    def toSumTree(self, root) :
        def dfs(root):
            if not root: return 0
            last = root.data
            root.data = dfs(root.left) + dfs(root.right)
            return root.data + last
            
        dfs(root)
        return root
