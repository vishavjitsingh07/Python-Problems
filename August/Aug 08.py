class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        dp = []
        tails = []

        for obstacle in obstacles:
            if not dp or obstacle >= dp[-1]:
                dp.append(obstacle)
                tails.append(len(dp) - 1)
            else:
                idx = bisect_right(dp, obstacle)
                dp[idx] = obstacle
                tails.append(idx)
        tails = [x+1 for x in tails]
        return tails
