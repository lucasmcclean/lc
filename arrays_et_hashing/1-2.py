class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matches = dict()

        for i in range(len(nums)):
            if nums[i] in matches:
                return [matches[nums[i]], i]
            matches[target - nums[i]] = i
