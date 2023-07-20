from collections import Counter
class Solution:
    def nonrepeatingCharacter(self,s):
        c = Counter(s)
        for i in s: if c[i] == 1: return i
        return "$"
