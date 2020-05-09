class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, value1 in enumerate(nums):
            numNeeded = target - value1
            if numNeeded in nums:
                numNeededIndex = nums.index(numNeeded)
                if index1 != numNeededIndex:
                    return [index1,numNeededIndex]
