class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, x - y)

        try:
            return -heapq.heappop(stones)
        except:
            return 0
