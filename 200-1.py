class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def flood_fill(r: int, c: int) -> None:
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            flood_fill(r - 1, c)
            flood_fill(r + 1, c)
            flood_fill(r, c - 1)
            flood_fill(r, c + 1)

        res = 0
        for r in range(len(grid)):
            for c in range (len(grid[r])):
                if grid[r][c] == "1":
                    res += 1
                    flood_fill(r, c)

        return res
