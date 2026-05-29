class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses

        for c, p in prerequisites:
            graph[p].append(c)
            degree[c] += 1

        order = []

        dq = deque(i for i in range(numCourses) if degree[i] == 0)
        while dq:
            p = dq.popleft()
            order.append(p)

            for c in graph[p]:
                degree[c] -= 1
                if degree[c] == 0:
                    dq.append(c)

        return order if len(order) == numCourses else []
