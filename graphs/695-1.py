class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def island_size(r: int, c: int) -> int:
            grid[r][c] = 0

            size = 0
            if r - 1 >= 0 and grid[r - 1][c] == 1:
                size += island_size(r - 1, c)
            if r + 1 < len(grid) and grid[r + 1][c] == 1:
                size += island_size(r + 1, c)
            if c - 1 >= 0 and grid[r][c - 1] == 1:
                size += island_size(r, c - 1)
            if c + 1 < len(grid[0]) and grid[r][c + 1] == 1:
                size += island_size(r, c + 1)

            return 1 + size

        max_size = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_size = max(island_size(r, c), max_size)

        return max_size
