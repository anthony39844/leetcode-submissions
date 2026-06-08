class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0, 0)]
        out = 0
        visited = set()

        def calc(start, end):
            x1, y1 = points[start]
            x2, y2 = points[end]
            return abs(x1- x2) + abs(y1 - y2)

        while len(visited) < len(points):
            dist, point = heapq.heappop(heap)
            if point in visited:
                continue
            visited.add(point)
            out += dist

            for i in range(len(points)):
                if i not in visited:
                    new_dist = calc(point, i)
                    heapq.heappush(heap, (new_dist, i))

        return out

