class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        courses = defaultdict(list)
        degree = [0] * numCourses
        taken = 0

        # make graph and 
        # degree list -> course 0 = degree 0 means no prereqs
        for course, prereq in prerequisites:
            courses[prereq].append(course)
            degree[course] += 1
        
        # init queue with classes with no prereqs
        q = deque()
        for i in range(len(degree)):
            if degree[i] == 0:
                q.append(i)
        
        while q:
            prereq = q.popleft()
            taken += 1

            # loop through classes with this prereq, dec their degree
            for course in courses[prereq]:
                degree[course] -= 1

                if degree[course] == 0:
                    q.append(course)
        
        return taken == numCourses

       

        
