class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def solve(idx: int, cur: int):
            if idx == len(nums) and cur == target:
                return 1
            if idx >= len(nums):
                return 0
            if (idx, cur) in memo:
                return memo[(idx, cur)]

            memo[(idx, cur)] = (
                solve(idx + 1, cur + nums[idx]) +
                solve(idx + 1, cur - nums[idx])
            )

            return memo[(idx, cur)]

        return solve(0, 0)
