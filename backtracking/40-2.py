class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()

        def generate(idx: int, comb: List[int], target: int) -> None:
            if target < 0:
                return
            elif target == 0:
                combinations.append(comb.copy())
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                elif candidates[i] > target:
                    break

                comb.append(candidates[i])
                generate(i + 1, comb, target - comb[-1])
                comb.pop()

        generate(0, [], target)
        return combinations
