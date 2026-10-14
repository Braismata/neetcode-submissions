class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        l,r=0,len(nums)-1
        m=(r+l)//2
        if nums[l]<nums[r]:
            return nums[l]
        while l<r:
            if nums[m]>nums[r]: 
                l=m+1
                m=(r+l)//2
            else:
                r=m
                m=(r+l)//2
        n=nums[l]
        return n
