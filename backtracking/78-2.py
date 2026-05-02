class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subset = []

        def generate(idx: int) -> None:
            if idx == len(nums):
                subsets.append(subset.copy())
                return

            subset.append(nums[idx])
            generate(idx + 1)

            subset.pop()
            generate(idx + 1)

        generate(0)
        return subsets
