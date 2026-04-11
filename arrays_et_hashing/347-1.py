class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        max_freq = max(counter.values())
        buckets = [[] for _ in range(max_freq)]

        for num, freq in counter.items():
            buckets[freq - 1].append(num)

        res = []
        for bucket in reversed(buckets):
            res.extend(bucket)
            if len(res) >= k:
                return res
