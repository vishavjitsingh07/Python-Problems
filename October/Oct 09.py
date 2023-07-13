class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
            indegree[pre[0]] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        visited = 0
        while q:
            n = q.popleft()
            visited += 1

            for nbr in adj[n]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)

        return visited == numCourses
