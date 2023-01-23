class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = set()
        for i, j in trust:
            people.add(i)
        if len(people) != n-1: return -1

        judge = -1
        for i in range(1, n+1):
            if i not in people:
                judge = i

        trustLen = 0
        for i, j in trust:
            if j == judge: trustLen +=1
            if i != judge: continue
            return -1
        print(judge, trustLen)
        return judge if trustLen == n-1 else -1
