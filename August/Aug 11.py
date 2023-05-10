class Solution:
    def generateMatrix(self, n):
        nums = [[0] * n for _ in range(n)] 
        startX, startY = 0, 0
        count = 1

        for offset in range(1, (n//2)+1):           
            for i in range(startY, n-offset):
                nums[startX][i] = count
                count += 1
            for i in range(startX, n-offset):
                nums[i][n-offset] = count
                count += 1
            for i in range(n-offset, startY, -1):
                nums[n-offset][i] = count
                count += 1
            for i in range(n-offset, startX, -1):
                nums[i][startY] = count
                count += 1
            
            startX += 1 
            startY += 1
            offset += 1

        if (n % 2) != 0:
            nums[n//2][n//2] = count
        return nums
       
