class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()

        def generate(idx: int, comb: [int, List[int]]) -> None:
            if idx == len(candidates) or comb[0] >= target:
                if comb[0] == target:
                    combinations.append(comb[1].copy())
                return

            cur = candidates[idx]

            comb[0] += cur
            comb[1].append(cur)
            generate(idx + 1, comb)
            comb[1].pop()
            comb[0] -= cur

            idx += 1
            while idx < len(candidates) and candidates[idx] == candidates[idx - 1]:
                idx += 1

            generate(idx, comb)

        generate(0, [0, []])
        return combinations
