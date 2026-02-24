class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def rec(idx: int, remaining: int) -> int:
            if remaining == 0:
                return 0
            if remaining < 0 or idx == len(coins):
                return float("inf")

            if (idx, remaining) in memo:
                return memo[(idx, remaining)]

            take = 1 + rec(idx, remaining - coins[idx])
            skip = rec(idx + 1, remaining)

            memo[(idx, remaining)] = min(take, skip)
            return memo[(idx, remaining)]

        res = rec(0, amount)
        return res if res != float("inf") else -1
