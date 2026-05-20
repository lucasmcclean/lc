class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0

        idx = 0
        while idx < len(nums) - 1:
            if idx + nums[idx] >= len(nums) - 1:
                jumps += 1
                break

            dist = 0
            for cnd in range(idx + 1, idx + nums[idx] + 1):
                if cnd + nums[cnd] > dist:
                    dist = cnd + nums[cnd]
                    idx = cnd

            jumps += 1

        return jumps
