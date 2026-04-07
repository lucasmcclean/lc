class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))

        visited = [float("inf")] * n

        heap = [(0, src, 0)]
        while heap:
            cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return cost

            if stops > k or visited[node] <= stops:
                continue
            visited[node] = stops

            for nxt, price in graph[node]:
                heapq.heappush(heap, (cost + price, nxt, stops + 1))

        return -1
