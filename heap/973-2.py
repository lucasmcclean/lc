class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = [[0, 0] for _ in range(k)]

        heap = []
        for i, point in enumerate(points):
            x, y = point
            distance = x**2 + y**2
            val = (distance, i)
            if len(heap) < k:
                heapq.heappush_max(heap, val)
            else:
                heapq.heappushpop_max(heap, val)

        for idx, val in enumerate(heap):
            _, i = val
            closest[idx] = points[i]

        return closest
