class Solution:

    def __init__(self):
        self.res = []

    def create_subsets(self, nums, idx, subset):
        if idx == len(nums):
            self.res.append(subset.copy())
            return
        
        self.create_subsets(nums, idx + 1, subset)

        subset.append(nums[idx])
        self.create_subsets(nums, idx + 1, subset)
        subset.pop()
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.create_subsets(nums, 0, [])
        return self.res
