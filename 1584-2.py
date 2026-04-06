class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = [float("inf")] * len(points)
        visited = [False] * len(points)

        dist[0] = 0
        cost = 0

        for _ in range(len(points)):
            short = -1
            for i in range(len(points)):
                if not visited[i] and (short == -1 or dist[i] < dist[short]):
                    short = i

            visited[short] = True
            cost += dist[short]

            for nxt in range(len(points)):
                if not visited[nxt]:
                    nxtDist = abs(points[short][0] - points[nxt][0]) + abs(points[short][1] - points[nxt][1])
                    dist[nxt] = min(dist[nxt], nxtDist)

        return cost
