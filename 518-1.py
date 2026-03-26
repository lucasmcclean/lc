class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = dict()

        def num_combinations(amount: int, idx: int) -> int:
            if amount < 0 or idx == len(coins):
                return 0
            if amount == 0 :
                return 1

            if (amount, idx) in memo:
                return memo[(amount, idx)]

            take = num_combinations(amount - coins[idx], idx)
            skip = num_combinations(amount, idx + 1)

            memo[(amount, idx)] = take + skip
            return memo[(amount, idx)]

        return num_combinations(amount, 0)
