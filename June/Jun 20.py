class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 0, 10**15
        def good(target):
            temp = 0
            for x in time:
                temp+= target//x
            return temp>=totalTrips
        while left<right:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid+1
        return left
