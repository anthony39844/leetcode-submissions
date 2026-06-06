class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0

        for start, end, time in times:
            graph[start].append((end, time))
        
        q = [(0, k)]
        visited = set()

        while q:
            dist, node = heapq.heappop(q)

            for x, time in graph[node]:
                new_time = dist + time
                if distances[x] > new_time and x not in visited:
                    distances[x] = new_time
                    heapq.heappush(q, (new_time, x))
                

        return max(distances.values()) if max(distances.values()) != float('inf') else -1
