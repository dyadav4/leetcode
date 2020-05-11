class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        judges = []
        non_judges = []
        if(len(trust) >= 1):
            for i in trust:
                if i[0] not in non_judges:
                    non_judges.append(i[0])

                if i[1] not in judges:
                    judges.append(i[1])
        else:
            judges.append(1)

        new_judges = []
        if len(judges) > 0 or len(non_judges) > 0:
            for i in judges:
                if i not in non_judges:
                    new_judges.append(i)

        if len(new_judges) == 1:
            judge = new_judges[0]
            for i in range(1,N+1):
                if i != new_judges[0]:
                    if [i,new_judges[0]] not in trust:
                        judge = -1
                        break
            return judge
        else:
            return -1
