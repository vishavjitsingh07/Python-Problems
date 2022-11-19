class Solution:
    def areAnagrams(self, node1 : Optional['Node'], node2 : Optional['Node']) -> bool:
        d1 = defaultdict(list)
        d2 = defaultdict(list)
        def dfs(root, level, d):
            if not root: return
            d[level].append(root.data)
            dfs(root.left, level+1, d)
            dfs(root.right, level+1, d)
            
        dfs(node1, 0, d1)
        dfs(node2, 0, d2)
        
        for i in d1:
            if i not in d2: return False
            if sorted(d1[i]) != sorted(d2[i]): 
                return False
        return True
