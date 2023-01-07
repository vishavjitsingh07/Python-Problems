class Solution():
    
    def flatten(self,root):
            curr = root
            def solve(dummy, root1, root2):
                if not root1:
                    dummy.bottom = root2
                    return
                if not root2:
                    dummy.bottom = root1
                    return
                if root1.data <= root2.data:
                    dummy.bottom = root1
                    solve(dummy.bottom,root1.bottom,root2)
                else:
                    dummy.bottom = root2
                    solve(dummy.bottom,root1,root2.bottom)
            def func(root):
                if not root: return None
                start = Node(-1)
                solve(start, root, func(root.next))
                root = start.bottom
                return root
            return func(root)
