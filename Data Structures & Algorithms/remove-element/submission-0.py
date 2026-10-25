class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=size=len(nums)
        l=0
        for i in range(size):
            if nums[i]==val:
                k-=1
            else:
                nums[l]=nums[i]
                l+=1
        return k