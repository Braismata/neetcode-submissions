class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:    return 0
        nums.sort()
        count=1
        max=0
        for n in range(len(nums)):
            if nums[n]==nums[n-1]+1:
                count+=1
            elif nums[n]>nums[n-1]:
                if count>max:
                    max=count
                count=1
        if count>max:   max=count
        return max
            