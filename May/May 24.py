class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        curr  = folder[0]
        ans = [curr]
        for i in folder[1:]:
            if curr+"/" in i[:len(curr)+1]: continue
            ans.append(i) 
            curr = i
        return ans
