class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        d = defaultdict(list)
        n = len(rooms)
        for room in range(n):
            for key in rooms[room]:
                d[room].append(key)

        visit = [False]*(n)
        visit[0] = True

        def dfs(node):
            if visit[node] == True: return
            visit[node] = True
            for i in d[node]:
                dfs(i)
                
        for i in d[0]:
            dfs(i)
        return False if False in visit else True
