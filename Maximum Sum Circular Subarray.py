
#this solution has O(n^2) complexity
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        startIndex = 0
        maxSum = min(A)
        
        while startIndex < len(A):
            
            loopSum = A[startIndex]
            for i in range(startIndex, startIndex+len(A)):

                if(startIndex == i):
                    loopSum = loopSum + 0
                else:
                    sumindex = i%len(A)
                    loopSum = loopSum + A[sumindex]

                if(loopSum > maxSum):
                    maxSum = loopSum

            startIndex = startIndex+1

        return maxSum
