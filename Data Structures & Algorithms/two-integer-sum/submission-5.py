class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashN={}
        for i, num in enumerate(nums):
        #for i in range(len(nums)):
            if target-num in HashN:
                return[HashN[target-num],i]
            HashN[num]=i
