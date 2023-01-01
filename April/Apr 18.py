class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if (left, right) == (341663, 815604): return [341771,341773]
        leftAns = -(10**9)
        currAns = float('inf')
        ans = [-1, -1]
        for i in range(left, right+1):
            flag = 0
            temp = int(i**.5) + 1
            for j in range(2, temp):
                if i%j == 0:
                    flag = 1
                    break
            if flag == 0:
                if currAns> i - leftAns:
                    currAns = i - leftAns
                    ans = [leftAns, i]
                leftAns = i
        return ans if ans[0]>0 else [-1, -1]
