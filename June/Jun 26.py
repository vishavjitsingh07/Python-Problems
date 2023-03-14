class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, str(root.val)))
        S = []
        while q:
            node, val = q.popleft()
            if not node.left and not node.right: S.append(int(val))
            if node.left: q.append((node.left, val + str(node.left.val)))
            if node.right: q.append((node.right, val + str(node.right.val)))
        return sum(S)
