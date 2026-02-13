class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def flood_fill(r: int, c: int) -> None:
            grid[r][c] = "0"

            if r - 1 >= 0 and grid[r - 1][c] == "1":
                flood_fill(r - 1, c)
            if r + 1 < len(grid) and grid[r + 1][c] == "1":
                flood_fill(r + 1, c)
            if c - 1 >= 0 and grid[r][c - 1] == "1":
                flood_fill(r, c - 1)
            if c + 1 < len(grid[0]) and grid[r][c + 1] == "1":
                flood_fill(r, c + 1)

        res = 0
        for r in range(len(grid)):
            for c in range (len(grid[r])):
                if grid[r][c] == "1":
                    res += 1
                    flood_fill(r, c)

        return res
