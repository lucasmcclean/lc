class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        def rob_sub(nums: List[int]) -> int:
            a = 0
            b = 0
            for n in nums:
                res = max(a, b + n)
                b, a = a, res
            return a

        return max(
            rob_sub(nums[1:]),
            rob_sub(nums[:-1])
        )
