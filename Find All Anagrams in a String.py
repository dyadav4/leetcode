


# this solution is O(n^2) complexity and not suitable
class Solution:
  
    def checkAnagram(self, index, s, p):
        newp = p
        
        
        for i in range(index,index+len(p)):
            #print(i)
            if(s[i] in newp):
                wordindex = newp.index(s[i])
                newp = newp[:wordindex] + newp[wordindex+1:]
                if newp == '':
                    return True
            else:
                return False
        
    
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        indexfoundlist = []
        for index in range(0, len(s)-len(p)+1):
            if s[index] in p:
                ifanagram = self.checkAnagram(index, s, p)
                if ifanagram:
                    indexfoundlist.append(index)
                    
        return indexfoundlist
