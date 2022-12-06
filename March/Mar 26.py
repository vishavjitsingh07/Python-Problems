class Solution:
    def KthSmallestElement(self, root, K):
        self.ans = [-1, 0]
        def dfs(root):
            if not root or self.ans[-1]>K: return
            dfs(root.left)
            if self.ans[-1] == K: return self.ans
            elif self.ans[-1]<K: self.ans =[root.data, self.ans[-1]+1]
            dfs(root.right)
            
        dfs(root)
        return -1 if self.ans[-1]!=K else self.ans[0]
