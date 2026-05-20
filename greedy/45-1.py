class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        dist = 0
        jumps = 0

        for i in range(len(nums) - 1):
            dist = max(i + nums[i], dist)

            if i == end:
                end = dist
                jumps += 1

        return jumps
