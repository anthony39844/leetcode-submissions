class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        # distance map, init start node to 0
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0

        # adjacency list
        for start, end, time in times:
            graph[start].append((end, time))
        
        q = [(0, k)]

        while q:
            dist, node = heapq.heappop(q)

            # optimize, if node takes longer to get to than stated in map, skip
            if dist > distances[node]:
                continue

            for x, time in graph[node]:
                new_time = dist + time
                # if the distance to this neighbor is less than stated in the map, update map add to q to potentially find neighbors with a smaller distance as well
                if distances[x] > new_time:
                    distances[x] = new_time
                    heapq.heappush(q, (new_time, x))
                
        # max value is the longest time it would take for signal to travel through graph, if there is an inf, that means there is a node that is unreachable
        return max(distances.values()) if max(distances.values()) != float('inf') else -1
