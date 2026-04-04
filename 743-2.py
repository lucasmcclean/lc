class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minTimes = [float("inf")] * (n + 1)
        minTimes[k] = 0

        for _ in range(n - 1):
            for u, v, w in times:
                if minTimes[u] + w < minTimes[v]:
                    minTimes[v] = minTimes[u] + w

        res = max(minTimes[1:])
        return res if res < float("inf") else -1
