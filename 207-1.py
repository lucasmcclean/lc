class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = dict()

        for course, pre in prerequisites:
            prereqs.setdefault(course, list())
            prereqs[course].append(pre)

        taken = set()

        def dfs(course: int):
            prereqs.setdefault(course)
            if not prereqs[course]:
                return True
            if course in taken:
                return False

            taken.add(course)
            for pre in prereqs[course]:
                if not dfs(pre):
                    return False

            prereqs[course] = None
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
