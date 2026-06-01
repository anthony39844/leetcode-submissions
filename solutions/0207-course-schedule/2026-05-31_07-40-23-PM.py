class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        courses = defaultdict(list)
        degree = [0] * numCourses
        taken = 0
        for course, prereq in prerequisites:
            courses[prereq].append(course)
            degree[course] += 1
        
        q = deque()
        for i in range(len(degree)):
            if degree[i] == 0:
                q.append(i)
        
        while q:
            x = q.popleft()
            taken += 1

            for i in courses[x]:
                degree[i] -= 1

                if degree[i] == 0:
                    q.append(i)
        
        return taken == numCourses

       

        
