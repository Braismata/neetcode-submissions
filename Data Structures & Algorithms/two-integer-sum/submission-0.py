class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index={} 
        for i in range(len(nums)):
            if (index.get(target-nums[i])!= None):
                return [index.get(target-nums[i]),i]
            index[nums[i]]=i
            