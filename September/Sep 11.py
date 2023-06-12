class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums+=[2147483649];f=[];a='';v=False
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                if not v:
                    a=str(nums[i])+'-'+'>';v=True
            else :
                a+=str(nums[i])
                f.append(a)
                a='';v=False
        return f
