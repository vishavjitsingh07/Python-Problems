class Solution:
    def findDuplicateSubtrees(self, root):
        result, dict1 = [], defaultdict(int)
        
        def dfs(node):
            if not node:
                return "None"
            
            path = str(node.val)
            path += "." + dfs(node.left)
            path += "." + dfs(node.right)
            
            dict1[path] += 1
            if dict1[path] == 2:
                result.append(node)
                
            return path
        
        dfs(root)
        return result
