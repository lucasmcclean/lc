class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            update = prices.copy()
            for u, v, w in flights:
                if prices[u] == float("inf"):
                    continue
                update[v] = min(update[v], prices[u] + w)
            prices = update

        return -1 if prices[dst] == float("inf") else prices[dst]
