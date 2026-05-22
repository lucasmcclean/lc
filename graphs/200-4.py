class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def visit(r: int, c: int) -> None:
            grid[r][c] = "#"

            if r - 1 >= 0 and grid[r - 1][c] == "1":
                visit(r - 1, c)
            if r + 1 < m and grid[r + 1][c] == "1":
                visit(r + 1, c)
            if c - 1 >= 0 and grid[r][c - 1] == "1":
                visit(r, c - 1)
            if c + 1 < n and grid[r][c + 1] == "1":
                visit(r, c + 1)

        islands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    islands += 1
                    visit(r, c)

        return islands
