class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mid_value=len(nums)//2
        nums.sort()
        return nums[mid_value]