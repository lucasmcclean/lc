class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = 0
        a, b = 0, 0
        for i in range(2, len(cost) + 1):
            one = cost[i - 1] + a
            two = cost[i - 2] + b
            res = min(one, two)
            b, a = a, res
        return res
