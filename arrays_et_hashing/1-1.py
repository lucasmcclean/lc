class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in complements:
                return [complements[comp], i]
            complements[nums[i]] = i

        print("uh oh")
