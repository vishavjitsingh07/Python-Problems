class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = collections.deque()
        q.append(entrance + [0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        n, m = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = "+"

        while q:
            elei, elej, currDis = q.popleft()
            for i, j in directions:
                nextI, nextJ = elei + i, elej + j

                if 0 <= nextI < n and 0 <= nextJ < m and maze[nextI][nextJ] == ".":
                    if (nextI == 0 or nextI == n-1 or nextJ == m-1 or nextJ == 0):
                        return currDis + 1
                    maze[nextI][nextJ] = "+"
                    q.append([nextI, nextJ, currDis + 1])

        return -1
