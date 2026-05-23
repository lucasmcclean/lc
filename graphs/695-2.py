class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        maxArea = 0

        def area(r: int, c: int) -> int:
            if (
                r < 0
                or c < 0
                or r >= m
                or c >= n
                or grid[r][c] != 1
            ):
                return 0

            grid[r][c] = 0
            return 1 + area(r - 1, c) + area(r + 1, c) + area(r, c - 1) + area(r, c + 1)


        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, area(r, c))

        return maxArea
