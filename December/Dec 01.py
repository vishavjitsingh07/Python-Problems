class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)<=1000 or len(nums2)<=1000:
            arr = sorted(nums1+nums2)
            if len(arr)%2 == 1: return arr[len(arr)//2]
            else: return (arr[len(arr)//2] + arr[(len(arr)//2) - 1])/2
        def median(nums1, nums2):
            n = len(nums1)
            m = len(nums2)
            if n%2 == 0 and m%2 == 0:
                left1 = n//2 - 1
                left2 = m//2 - 1
            elif n%2 == 1 and m%2 == 1:
                left1 = n//2
                left2 = m//2 - 1
            elif n%2 == 1 and m%2 == 0:
                left1 = n//2
                left2 = m//2 - 1
            else:
                left1 = n//2
                left2 = m//2 - 1

            right1 = left1 + 1
            right2 = left2 + 1

            while 0<= left1< right1<n and 0<= left2< right2<m:
                if (nums1[left1]< nums2[right2]) and (nums2[left2]< nums1[right1]): break

                elif nums1[left1]>nums2[right2]:
                    right2 += 1
                    left1 -= 1
                    left2 +=1
                    right1 -=1
                else:
                    left1 +=1
                    left2 -=1
                    right1 +=1
                    right2 -=1
                if left1<0 or right1<n or right2<m or left2<0:
                    break

            
            if (n+m)%2 == 1:             
                if 0<=left1< n and 0<=left2<m:
                    val1 = max(nums1[left1], nums2[left2])
                elif 0<=left1<n:
                    val1 = nums1[left1]
                elif 0<= left2<n: 
                    val1 = nums2[left2] 
                return val1
                    
            else:
                if 0<=left1< n and 0<=left2<m:
                    val1 = max(nums1[left1], nums2[left2])
                elif 0<=left1<n:
                    val1 = nums1[left1]
                elif 0<= left2<n: 
                    val1 = nums2[left2]

                if 0<=right1< n and 0<=right2<m:
                    val2 = min(nums1[right1], nums2[right2])
                elif 0<=right1<n:
                    val2 = nums1[right1]
                else: 
                    val2 = nums2[right2]
                return (val1 + val2) / 2
    
    
        if len(nums2) >= len(nums1):
            return median(nums1, nums2)
        else:
            return median(nums2, nums1)
