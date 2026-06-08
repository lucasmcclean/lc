class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]

        def find_parent(x: int) -> int:
            if parent[x] != x:
                parent[x] = find_parent(parent[x])
            return parent[x]

        def union(x: int, y: int) -> bool:
            px = find_parent(x)
            py = find_parent(y)

            if px == py:
                return False

            parent[py] = px
            return True

        for x, y in edges:
            if not union(x, y):
                return [x, y]

        return []
