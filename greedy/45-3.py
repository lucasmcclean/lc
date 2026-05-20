class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0

        furthest, end = 0, 0
        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])

            if i == end:
                jumps += 1
                end = furthest

        return jumps
