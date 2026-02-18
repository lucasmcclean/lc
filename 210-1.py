class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            adj[course].append(prereq)

        handled = set()
        courses = list()
        taken = [0] * numCourses
        def dfs(course: int):
            if taken[course] == 1:
                return False
            if taken[course] == -1:
                return True

            taken[course] = 1
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False

            taken[course] = -1
            if course in handled:
                courses.remove(course)
            else:
                handled.add(course)
            courses.append(course)

            return True

        for course in range(numCourses):
            if taken[course] == 0:
                if not dfs(course):
                    return []

        return courses
