class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.latest = Node(0, 0)
        self.oldest = Node(0, 0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            p, n = node.prev, node.next
            p.next = n
            n.prev = p

            p, n = self.latest.prev, self.latest
            p.next = n.prev = node
            node.next = n
            node.prev = p
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            p, n = node.prev, node.next
            p.next = n
            n.prev = p

        node = self.cache[key] = Node(key, value)
        p, n = self.latest.prev, self.latest
        p.next = n.prev = node
        node.next = n
        node.prev = p

        if len(self.cache) > self.cap:
            lru = self.oldest.next
            p, n = lru.prev, lru.next
            p.next = n
            n.prev = p
            del self.cache[lru.key]
