class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0

        dq = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    dq.append((r, c))

        elapsed = 0
        while dq and fresh > 0:
            elapsed += 1

            count = len(dq)
            for _ in range(count):
                r, c = dq.popleft()

                for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nc < 0 or nr >= m or nc >= n:
                        continue
                    elif grid[nr][nc] != 1:
                        continue

                    fresh -= 1
                    grid[nr][nc] = 2
                    dq.append((nr, nc))

        return elapsed if fresh == 0 else -1
