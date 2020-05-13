class Solution:

    def removeKdigits(self, num: str, k: int) -> str:
        leastStr = ''
        if len(num) <= k:
            return '0'
        
        def getSmallNumIndex(index, num, reqlenStr):
            minNum = 10
            numIndex = index

            for i in range(index, (len(num)-(reqlenStr-1))):
                intNum = int(num[i])

                if intNum < minNum:
                    minNum = intNum
                    numIndex = i

            return numIndex

        initialIndex = 0
        while len(leastStr) < len(num)-k:
            leftK = k - len(leastStr)

            reqlenStr = len(num)-k-len(leastStr)
            newIndex = getSmallNumIndex(initialIndex, num, reqlenStr)
            initialIndex = newIndex+1
            leastStr = leastStr + num[newIndex]

        leastStr = int(leastStr)
        return str(leastStr)
