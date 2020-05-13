class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        singleE = ''
        
        for index in range(len(nums)):
            if index%2 == 1:
                if nums[index] != nums[index-1]:
                    singleE = nums[index-1]
                    break
                    
        if(type(singleE) == str):
            singleE = nums[len(nums)-1]
        
        return singleE
