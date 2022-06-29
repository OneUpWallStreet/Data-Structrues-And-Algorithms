from typing import List
import collections

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        rows = len(maze)
        cols = len(maze[0])

        result = -1
        q = collections.deque()

        q.append((entrance[0], entrance[1], 0))
        alreadyVisited = set()
        alreadyVisited.add((entrance[0], entrance[1]))

        while q:

            r, c, step = q.popleft()

            if (r == 0 or c == 0 or r == rows-1 or c == cols-1) and [r,c] != entrance:
                return step

            step += 1

            for dr, dc in directions:
                if (r + dr) in range(rows) and (c + dc) in range(cols) and \
                        maze[r + dr][c + dc] == '.' and (r + dr, c + dc) not in alreadyVisited:
                    alreadyVisited.add((r + dr, c + dc))
                    q.append((r + dr, c + dc, step))

        return -1