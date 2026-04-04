class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        heap = [(0, k)]
        times = {}

        while heap:
            curTime, node = heapq.heappop(heap)
            if node in times:
                continue

            times[node] = curTime

            for nxt, time in graph[node]:
                if nxt not in times:
                    heapq.heappush(heap, (curTime + time, nxt))

        return max(times.values()) if len(times) == n else -1
