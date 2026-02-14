class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_fresh = 0
        rotten = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    num_fresh += 1

        if num_fresh == 0:
            return 0
        elif len(rotten) == 0:
            return -1

        time = 0
        while len(rotten) > 0 and num_fresh > 0:
            time += 1
            num_rotten = len(rotten)
            for _ in range(num_rotten):
                r, c = rotten.popleft()
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    num_fresh -= 1
                    grid[r - 1][c] = 2
                    rotten.append((r - 1, c))
                if r + 1 < len(grid) and grid[r + 1][c] == 1:
                    num_fresh -= 1
                    grid[r + 1][c] = 2
                    rotten.append((r + 1, c))
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    num_fresh -= 1
                    grid[r][c - 1] = 2
                    rotten.append((r, c - 1))
                if c + 1 < len(grid[0]) and grid[r][c + 1] == 1:
                    num_fresh -= 1
                    grid[r][c + 1] = 2
                    rotten.append((r, c + 1))

        return -1 if num_fresh > 0 else time
