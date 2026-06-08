class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = [float('inf')] * len(points)
        distances[0] = 0
        out = 0
        visited = set()

        def find_next():
            idx = -1
            cur = float('inf')
            for i in range(len(distances)):
                if i not in visited and distances[i] < cur:
                    idx = i
                    cur = distances[i]
            
            return idx

        def calc(start, end):
            x1, y1 = points[start]
            x2, y2 = points[end]
            return abs(x1- x2) + abs(y1 - y2)

        for _ in range(len(points)):
            # find the next closest point (starts with the first point)
            point = find_next()
            visited.add(point)
            out += distances[point]

            # loop through every other point, calc the distance of that point from cur point, update distances arr
            for i in range(len(points)):
                if i not in visited:
                    dist = calc(point, i)
                    if dist < distances[i]:
                        distances[i] = dist
        
        return out

