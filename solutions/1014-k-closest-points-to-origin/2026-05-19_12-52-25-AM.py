class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (((x ** 2) + (y ** 2)) ** 0.5, (x, y)))
        
        out = []

        for i in range(k):
            out.append(heapq.heappop(heap)[1])
        
        return out
       

