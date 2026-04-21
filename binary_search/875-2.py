class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float("inf")

        l, r = 1, max(piles)
        while l <= r:
            k = l + (r - l) // 2
            time = reduce(lambda a, p: a - (-p // k), piles, 0)
            if time <= h:
                res = min(res, k)
                r = k - 1
            elif time > h:
                l = k + 1

        return res
