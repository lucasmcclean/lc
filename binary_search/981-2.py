class TimeMap:

    class Node:

        def __init__(self, timestamp: int, value: str, nxt: Optional[Node] = None):
            self.timestamp = timestamp
            self.value = value
            self.nxt = nxt

    def __init__(self):
        self.kv = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        nxt = None if key not in self.kv else self.kv[key]
        self.kv[key] = self.Node(timestamp, value, nxt)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv:
            return ""

        node = self.kv[key]
        while node:
            if node.timestamp <= timestamp:
                return node.value
            node = node.nxt

        return ""
