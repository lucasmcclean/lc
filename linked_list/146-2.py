class LRUCache:

    class Node:

        def __init__(
            self,
            key: int,
            prv: Optional[Node] = None,
            nxt: Optional[Node] = None
        ):
            self.key = key
            self.prv = prv
            self.nxt = nxt


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
        self.values = dict()


    def get(self, key: int) -> int:
        (val, node) = self.values.get(key, (-1, None))
        if val == -1:
            return -1

        self.delete(node)
        self.use(node)

        return val


    def put(self, key: int, value: int) -> None:
        if key in self.values:
            _, node = self.values[key]
            self.delete(node)
            self.use(node)
            self.values[key] = (value, node)
            return

        if self.size == self.capacity:
            del self.values[self.tail.key]
            self.delete(self.tail)
        else:
            self.size += 1

        node = self.Node(key)
        self.values[key] = (value, node)
        self.use(node)


    def delete(self, node: Node) -> None:
        if node.prv:
            node.prv.nxt = node.nxt
        else:
            self.head = node.nxt

        if node.nxt:
            node.nxt.prv = node.prv
        else:
            self.tail = node.prv


    def use(self, node: Node) -> None:
        node.prv = None
        node.nxt = self.head

        if self.head:
            self.head.prv = node
        self.head = node

        if self.tail is None:
            self.tail = node
