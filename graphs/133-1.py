from typing import Optional

class Solution:

    def __init__(self):
        self.visited = dict()

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        if node in self.visited:
            return self.visited[node]

        new = Node(node.val)
        self.visited[node] = new

        for nghbr in node.neighbors:
            new.neighbors.append(self.cloneGraph(nghbr))

        return new
