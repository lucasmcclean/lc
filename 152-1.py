class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        g_max = nums[0]
        p_min = nums[0]
        p_max = nums[0]

        for n in nums[1:]:
            t_max = max(n, n * p_max, n * p_min)
            p_min = min(n, n * p_max, n * p_min)
            p_max = t_max
            g_max = max(p_max, g_max)

        return g_max
