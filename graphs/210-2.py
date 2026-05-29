class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses

        for c, p in prerequisites:
            graph[c].append(p)
            degree[p] += 1

        order = []

        dq = deque(i for i in range(numCourses) if degree[i] == 0)
        while dq:
            c = dq.popleft()
            order.append(c)

            for p in graph[c]:
                degree[p] -= 1
                if degree[p] == 0:
                    dq.append(p)

        return order[::-1] if len(order) == numCourses else []
