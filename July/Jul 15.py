class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stck = []
        for i in path:
            if stck and i == "..":
                stck.pop()
            if i not in ["", ".", ".."]: stck.append(i)
        return "/"+ "/".join(stck)
