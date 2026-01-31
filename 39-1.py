class Solution:

    def __init__(self):
        self.res = []
        self.target = None
        self.cans = []

    def combinations(self, idx, cur):
        if sum(cur) == self.target:
            self.res.append(cur.copy())
            return
        elif sum(cur) > self.target or idx == len(self.cans):
            return

        cur.append(self.cans[idx])
        self.combinations(idx, cur)
        cur.pop()

        self.combinations(idx + 1, cur)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.cans = candidates
        self.combinations(0, [])
        return self.res
