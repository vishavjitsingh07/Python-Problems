from typing import List
class Solution:
    def makePalindrome(self, n : int, l : List[str]) -> bool:
        while len(l)>1:
            temp=l.pop()
            if temp[::-1] in l: l.remove(temp[::-1])
            else: return False
        return True if (len(l)==0 or l[0]==l[0][::-1]) else False
