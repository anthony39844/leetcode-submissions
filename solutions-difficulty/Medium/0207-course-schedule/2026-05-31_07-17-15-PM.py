class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        safe = set()
        visited = set()

        def dfs(course):
            if course in safe:
                return True
            if course in visited:
                return False

            visited.add(course)
            for i in prereqs[course]:
                if not dfs(i):
                    return False
            safe.add(course)
            visited.remove(course)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True
        

        
