class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cd, sell, hold = 0, 0, -float('inf')

        for price in prices:
            p_cd, p_sell, p_hold = cd, sell, hold
            cd = max(p_cd, p_sell)
            sell = p_hold + price
            hold = max(p_hold, p_cd - price)

        return max(sell, cd)
