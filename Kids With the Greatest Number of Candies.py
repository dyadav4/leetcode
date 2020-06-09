class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandie = max(candies)
        returnarr = []
        for kidcandie in candies:
            if(kidcandie+extraCandies>=maxcandie):
                returnarr.append(True)
            else:
                returnarr.append(False)
                
        
        return returnarr
