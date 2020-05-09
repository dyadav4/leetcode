class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        
        while (len(s) > 0):
            arr = []
            for char in s:
                if char in arr:
                    break
                else:
                    arr.append(char)
            
            length = len(arr)
            if length > maxLength:
                maxLength = length
            s = s[1:]
        
        return maxLength
