class Solution:
    
    def searcheleindex(self, nums: List[int], element: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start+end)//2
            if element == nums[mid]:
                return mid
            elif element < nums[mid]:
                end = mid-1
            else:
                start = mid+1
                
        return -1
    
    def inserteleindex(self, nums: List[int], element: int) -> int:
        startindex = 0
        endindex = len(nums)
        
        while endindex - startindex != 1:
            mid = (startindex+endindex)//2
            
            if nums[mid] < element:
                startindex = mid
                
            if nums[mid] > element:
                endindex = mid
        
        if element < nums[startindex]:
            return startindex
        else:
            return endindex
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        searchindex = self.searcheleindex(nums,target)
        if searchindex >= 0:
            return searchindex
        else:
            insertindex = self.inserteleindex(nums,target)
            return insertindex
