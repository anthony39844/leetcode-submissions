class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            degree[course] += 1

        q = deque()
        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)
        
        out = []
        while q:
            prereq = q.popleft()
            out.append(prereq)

            for course in graph[prereq]:
                degree[course] -= 1
                if degree[course] == 0:
                    q.append(course)
        
        if len(out) == numCourses:
            return out
        else:
            return []

        

