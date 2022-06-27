from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])

        alreadyVisited = set()

        def dfs(r, c):
            alreadyVisited.add((r, c))

            for (dr, dc) in directions:

                if (r + dr) in range(rows) and \
                        (c + dc) in range(cols) and \
                        grid[r + dr][c + dc] == str(1) and \
                        (r+dr,c+dc) not in alreadyVisited:
                    dfs(r + dr, c + dc)

        result = 0
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == str(1) and (i, j) not in alreadyVisited:
                    dfs(i, j)
                    result += 1

        return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    answer = solution.numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ])
    print("answer: ", answer)
