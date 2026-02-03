class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        k = sum(1 for c in counts.values() if c == max_freq)
        return max(len(tasks), (max_freq - 1) * (n + 1) + k)
