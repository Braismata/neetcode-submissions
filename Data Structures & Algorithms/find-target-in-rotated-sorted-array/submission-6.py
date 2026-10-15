class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1: return 0 if nums[0]==target else -1
        l,r=0,len(nums)-1
        while l<=r:
            m=(r+l)//2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
