class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(idx: int, total: int):
            if total == target:
                res.append(cur.copy())
                return

            if total > target or idx >= len(candidates):
                return

            cur.append(candidates[idx])
            dfs(idx, total + candidates[idx])
            cur.pop()

            dfs(idx + 1, total)

        dfs(0, 0)
        return res
