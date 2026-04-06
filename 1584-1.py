class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(i: int, j: int) -> int:
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        visited = set()
        heap = [(0, 0)]
        cost = 0

        while len(visited) < len(points):
            cur, node = heapq.heappop(heap)
            if node in visited:
                continue

            visited.add(node)
            cost += cur

            for nxt in range(len(points)):
                if nxt not in visited:
                    heapq.heappush(heap, (dist(node, nxt), nxt))

        return cost
