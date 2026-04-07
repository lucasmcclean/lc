class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        connections = [[] for _ in range(n)]
        for fr, to, pr in flights:
            connections[fr].append((to, pr))

        memo = {}
        def takeFlight(fr: int, k: int) -> int:
            if (fr, k) in memo:
                return memo[(fr, k)]
            if fr == dst:
                return 0
            if k < 0:
                return float("inf")

            minPrice = float("inf")
            for to, pr in connections[fr]:
                cost = takeFlight(to, k - 1)
                if cost != float("inf"):
                    minPrice = min(minPrice, pr + cost)

            memo[(fr, k)] = minPrice

            return minPrice

        price = takeFlight(src, k)
        return price if price != float("inf") else -1
