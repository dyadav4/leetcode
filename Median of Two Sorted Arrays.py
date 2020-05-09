class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        median = 0
        if len(nums3)%2 == 0:
            mid2NumIndex = int(len(nums3)/2)
            median = (nums3[mid2NumIndex] + nums3[mid2NumIndex-1])/2
        else:
            midIndex = math.floor(len(nums3)/2)
            median = nums3[midIndex]
            
        return median
