# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        first_bad = n
        while start<end:
            mid = (start+end)//2
            if isBadVersion(mid) == False and isBadVersion(mid+1):
                first_bad = mid+1
                break
            elif isBadVersion(mid) == False and isBadVersion(mid+1) == False:
                start = mid
            elif isBadVersion(mid) and isBadVersion(mid-1) == False:
                first_bad = mid
                break
            else:
                end = mid
            
            
        return first_bad
