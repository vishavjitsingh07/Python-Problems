class Solution:
    def height(self, root):
        self.height = 0
        def dfs(root, level):
            if not root:
                return None
            self.height = max(level, self.height)
            dfs(root.left, level+1), dfs(root.right, level+1)
        dfs(root, 1)
        return self.height
