class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        heap = [(grid[0][0], 0, 0)]

        while heap:
            curTime, r, c = heapq.heappop(heap)

            if visited[r][c]:
                continue

            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return curTime

            visited[r][c] = True

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or visited[nr][nc]:
                    continue
                heapq.heappush(heap, (max(curTime, grid[nr][nc]), nr, nc))

        return -1 # Should be unreachable
