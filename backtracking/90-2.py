class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        cur = []
        nums.sort()

        def generate(idx: int) -> None:
            if idx == len(nums):
                subsets.append(cur.copy())
                return

            cur.append(nums[idx])
            generate(idx + 1)
            cur.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            generate(idx + 1)

        generate(0)
        return subsets
