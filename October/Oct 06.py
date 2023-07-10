class Solution:
    def minDepth(self, root: []) -> int:
        q = [(root, 1)]
        while q:
            node, depth = q.pop(0)
            if node is None:
                continue
            if not (node.left or node.right):
                return depth
            q.append((node.left, depth + 1))
            q.append((node.right, depth + 1))
        return 0
