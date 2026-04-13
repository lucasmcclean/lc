class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][0] > h:
                height, index = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index

            stack.append((h, start))

        n = len(heights)
        for height, index in stack:
            maxArea = max(maxArea, height * (n - index))

        return maxArea
