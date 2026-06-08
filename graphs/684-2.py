class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> bool:
            pa, pb = find(a), find(b)

            if pa == pb:
                return False

            parent[pa] = pb
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
