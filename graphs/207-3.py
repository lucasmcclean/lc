class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = dict()
        for c, p in prerequisites:
            prereqs.setdefault(c, list())
            prereqs[c].append(p)

        taken = set()

        def hasCycle(course: int) -> bool:
            prereqs.setdefault(course, list())
            if not prereqs[course]:
                return False

            if course in taken:
                return True

            taken.add(course)

            for p in prereqs[course]:
                if hasCycle(p):
                    return True

            prereqs[course] = []
            return False

        for course in range(numCourses):
            if hasCycle(course):
                return False

        return True
