class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 0
        mn, mx = 1, max(piles)
        while mn <= mx:
            mid = mn + (mx - mn) // 2

            h_left = h
            for pile in piles:
                h_left -= (pile + mid - 1) // mid
                if h_left < 0:
                    break

            if h_left < 0:
                mn = mid + 1
            else:
                k = mid
                mx = mid - 1

        return k
