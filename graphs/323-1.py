class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visited = [False] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            for neigh in graph[node]:
                if not visited[neigh]:
                    visited[neigh] = True
                    dfs(neigh)

        components = 0
        for node in range(n):
            if not visited[node]:
                components += 1
                visited[node] = True
                dfs(node)

        return components
