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
        while dq:
            count = len(dq)
            for _ in range(count):
                r, c = dq.popleft()
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    fresh -= 1
                    grid[r - 1][c] = 2
                    dq.append((r - 1, c))
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    fresh -= 1
                    grid[r][c - 1] = 2
                    dq.append((r, c - 1))
                if r + 1 < m and grid[r + 1][c] == 1:
                    fresh -= 1
                    grid[r + 1][c] = 2
                    dq.append((r + 1, c))
                if c + 1 < n and grid[r][c + 1] == 1:
                    fresh -= 1
                    grid[r][c + 1] = 2
                    dq.append((r, c + 1))
            if dq:
                elapsed += 1

        return elapsed if fresh == 0 else -1
