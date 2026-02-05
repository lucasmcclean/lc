class Solution:
    def generate(self, nums: List[int], idx: int) -> List[List[int]]:
        if idx == len(nums):
            return [nums.copy()]

        res = []
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            res.extend(self.generate(nums, idx + 1))
            nums[idx], nums[i] = nums[i], nums[idx]

        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.generate(nums, 0)
