class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0

        lmx, rmx = 0, 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] < height[r]:
                if height[l] >= lmx:
                    lmx = height[l]
                else:
                    trapped += lmx - height[l]
                l += 1
            else:
                if height[r] >= rmx:
                    rmx = height[r]
                else:
                    trapped += rmx - height[r]
                r -= 1

        return trapped
