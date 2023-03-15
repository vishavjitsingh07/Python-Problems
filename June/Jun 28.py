class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        Flag = False
        while q:
            node = q.popleft()
            if not node:  
                Flag = True
                continue
            if Flag: return False
            q.append(node.left), q.append(node.right)
        return True
