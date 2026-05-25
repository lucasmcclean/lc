class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m, n = len(grid), len(grid[0])

        dq = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    dq.append((r, c))

        while dq:
            r, c = dq.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if (
                    nr < 0
                    or nc < 0
                    or nr >= m
                    or nc >= n
                    or grid[nr][nc] != INF
                ):
                    continue

                grid[nr][nc] = grid[r][c] + 1
                dq.append((nr, nc))
