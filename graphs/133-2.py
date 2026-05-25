from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = dict()

        def dfs(node: Optional['Node']) -> Optional['Node']:
            if node is None:
                return None
            if node.val in nodes:
                return nodes[node.val]

            clone = Node()
            clone.val = node.val
            nodes[clone.val] = clone

            for neigh in node.neighbors:
                if neigh.val in nodes:
                    clone.neighbors.append(nodes[neigh.val])
                else:
                    clone.neighbors.append(dfs(neigh))

            return clone

        clone = dfs(node)
        return clone
