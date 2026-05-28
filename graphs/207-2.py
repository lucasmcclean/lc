class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            adj[course].append(pre)

        taken = [0] * numCourses
        def valid(course: int):
            if taken[course] == 1:
                return False
            if taken[course] == -1:
                return True

            taken[course] = 1
            for pre in adj[course]:
                if not valid(pre):
                    return False

            taken[course] = -1
            return True


        for course in range(numCourses):
            if taken[course] == 0 and not valid(course):
                return False

        return True
