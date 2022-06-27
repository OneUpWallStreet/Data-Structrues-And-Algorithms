from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows = len(image) - 1
        cols = len(image[0]) - 1
        startingColor = image[sr][sc]

        if image[sr][sc] == color:
            return image

        def dfs(r, c):

            if r < 0 or c < 0 or r > rows or c > cols or image[r][c] != startingColor:
                return

            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image


if __name__ == '__main__':
    solution = Solution()
    answer = solution.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
    print("Answer: ", answer)
