class Solution:
    def nextLargerElement(self,nums,n):
        st, res = [], [-1]*len(nums)
        for idx, i in enumerate(nums):
            while st and (nums[st[-1]] < i):
                res[st.pop()] = i
            if idx < len(nums):
                st.append(idx)
        return res
