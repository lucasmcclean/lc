class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def generate(idx: int, subset: List[int]) -> List[int]:
            if idx == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[idx])
            generate(idx + 1, subset)
            subset.pop()

            idx += 1
            while idx < len(nums) and nums[idx] == nums[idx - 1]:
                idx += 1

            generate(idx, subset)

        generate(0, [])
        return res
