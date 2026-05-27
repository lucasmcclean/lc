class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        def visitPeaks(r: int, c: int, visited: List[List[int]]):
            visited.add((r, c))

            if (
                r - 1 >= 0
                and heights[r - 1][c] >= heights[r][c]
                and (r - 1, c) not in visited
            ):
                visitPeaks(r - 1, c, visited)
            if (
                r + 1 < len(heights)
                and heights[r + 1][c] >= heights[r][c]
                and (r + 1, c) not in visited
            ):
                visitPeaks(r + 1, c, visited)
            if (
                c - 1 >= 0
                and heights[r][c - 1] >= heights[r][c]
                and (r, c - 1) not in visited
            ):
                visitPeaks(r, c - 1, visited)
            if (
                c + 1 < len(heights[0])
                and heights[r][c + 1] >= heights[r][c]
                and (r, c + 1) not in visited
            ):
                visitPeaks(r, c + 1, visited)

        for c in range(len(heights[0])):
            visitPeaks(0, c, pacific)
        for c in range(len(heights[0])):
            visitPeaks(len(heights) - 1, c, atlantic)
        for r in range(len(heights)):
            visitPeaks(r, 0, pacific)
        for r in range(len(heights)):
            visitPeaks(r, len(heights[0]) - 1, atlantic)

        return list(pacific & atlantic)
