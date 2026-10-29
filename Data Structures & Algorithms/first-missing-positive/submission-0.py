class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        visited=[]
        first_missing=1
        for i in range(len(nums)):
            if nums[i]==first_missing:
                first_missing +=1
                while first_missing in visited:
                    first_missing +=1
            else:
                visited.append(nums[i])
        return first_missing