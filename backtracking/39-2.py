class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def createCombinations(idx: int, subset: List[int]):
            if sum(subset) == target:
                combinations.append(subset.copy())
                return
            elif sum(subset) > target or idx == len(candidates):
                return

            subset.append(candidates[idx])
            createCombinations(idx, subset)
            subset.pop()

            createCombinations(idx + 1, subset)

        createCombinations(0, [])
        return combinations
