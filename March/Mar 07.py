class Solution:
    def longestPerfectPiece(self, arr, N):
        s = SortedList([])
        ans = 0
        i = 0
        j = 0
        while i < N:
            s.add(arr[i])
            while s[-1] - s[0] > 1:
                s.remove(arr[j])
                j += 1
            ans = max(ans, len(s))
            i += 1
        return ans
