class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(curr, parr):
            if not curr: return False, True
            c1, m1 = dfs(curr.left, curr)
            c2, m2 = dfs(curr.right, curr)
            cam, mon = False, False
            if c1 or c2:
                mon = True
            if not m1 or not m2:
                print(self.ans)
                self.ans +=1
                mon = cam = True
            return cam, mon
        c, m = dfs(root, -1)
        if not m: self.ans+=1
        return self.ans
