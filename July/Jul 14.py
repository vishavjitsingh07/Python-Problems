class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)
        arr = []
        arr2 = []
        for i in s:
            if i == "*" and len(arr)>0:
                arr.pop()
            elif i == "*" and len(arr)<=0:
                arr2.append(i)
            else:
                arr.append(i)
            while arr2 and arr:
                arr2.pop()
                arr.pop()

        return "".join(arr)
