class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashN={}
        for i in range(len(nums)):
            if target-nums[i] in HashN:
                return[HashN[target-nums[i]],i]
            HashN[nums[i]]=i
