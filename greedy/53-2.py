class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        c = 0

        for n in nums:
            if c < 0:
                c = 0
            c += n
            if c > m:
                m = c

        return m
