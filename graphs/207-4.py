class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        inDegree = [0] * numCourses

        for c, p in prerequisites:
            graph[c].append(p)
            inDegree[p] += 1

        taken = 0
        dq = deque(
            i for i in range(numCourses) if inDegree[i] == 0
        )

        while dq:
            course = dq.popleft()
            taken += 1

            for i in graph[course]:
                inDegree[i] -= 1
                if inDegree[i] == 0:
                    dq.append(i)

        return taken == numCourses
