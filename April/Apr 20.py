#User function Template for python3
import bisect
class Solution:
    def removeStudents(self, nums, N):
        temp = [nums[0]]
        for i in nums:
            x = bisect.bisect_left(temp, i)
            if x == len(temp): temp.append(i)
            elif i<temp[x]: temp[x] = i
        return N-len(temp)
