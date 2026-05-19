class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running = 0
        cur = nums[0]

        for num in nums:
            if running < 0:
                running = 0

            running += num
            cur = max(cur, running)

        return cur
