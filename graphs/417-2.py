class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def bfs(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            visited = set(starts)
            dq = deque(starts)

            while dq:
                r, c = dq.popleft()

                for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    nr, nc = r + dr, c + dc

                    if(
                        nr < 0
                        or nr >= m
                        or nc < 0
                        or nc >= n
                        or (nr, nc) in visited
                        or heights[nr][nc] < heights[r][c]
                    ):
                        continue

                    visited.add((nr, nc))
                    dq.append((nr, nc))

            return visited

        pacific = [(r, 0) for r in range(m)] + [(0, c) for c in range(n)]
        atlantic = [(r, n - 1) for r in range(m)] + [(m - 1, c) for c in range(n)]

        p = bfs(pacific)
        a = bfs(atlantic)
        return sorted(a & p)
