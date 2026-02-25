class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        dist = 0
        i = len(nums) - 1
        while i >= 0:
            i -= 1
            dist = 1
            while i >= 0 and nums[i] < dist:
                i -= 1
                dist += 1

        return nums[i+1] >= dist
