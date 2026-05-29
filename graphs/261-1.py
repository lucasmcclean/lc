class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def dfs(to, fr):
            if to in visited:
                return False

            visited.add(to)
            for neigh in graph[to]:
                if neigh == fr:
                    continue
                if not dfs(neigh, to):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
