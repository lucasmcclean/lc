class TimeMap:

    def __init__(self):
        self.pairs = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.pairs.setdefault(key, [])
        self.pairs[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.pairs:
            return ""
        values = self.pairs[key]
        res = ""
        l, r = 0, len(values) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
