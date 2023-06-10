from typing import List


class Solution:
    def Rearrange(self, n : int, arr : List[int]) -> None:
        li1 = []
        li2 = []
        for i in arr:
            if i < 0:
                li1.append(i)
            elif i >= 0:
                li2.append(i)
        arr[:] = li1 + li2
        # code here
        

