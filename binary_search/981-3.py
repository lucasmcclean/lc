class TimeMap:

    def __init__(self):
        self.kv = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv:
            self.kv[key] = []
        self.kv[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv:
            return ""

        values = self.kv[key]

        value = ""
        l, r = 0, len(values) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if values[mid][0] <= timestamp:
                value = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return value
