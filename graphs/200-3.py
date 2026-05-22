class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        visited = set()

        def visit(r: int, c: int) -> None:
            visited.add((r, c))
            for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n or (nr, nc) in visited or grid[nr][nc] == "0":
                    continue
                visit(nr, nc)

        islands = 0
        for r in range(m):
            for c in range(n):
                if (r, c) in visited:
                    continue

                if grid[r][c] == "1":
                    islands += 1
                    visit(r, c)

        return islands
