class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        # keeps track of most frequent tasks, process most frequent ones first
        heap = [v for v in counts.values()]
        heapq.heapify_max(heap)

        # keeps track of the cooldown for tasks
        q = deque()
        time = 0

        while heap or q:
            time += 1

            # if task if off cooldown, add back to heap
            if q and q[0][1] == time:
                x, _ = q.popleft()
                heapq.heappush_max(heap, x)

            # if there are any tasks to process, decrement their freq and add to queue
            if heap:
                x = heapq.heappop_max(heap) - 1
                if x > 0:
                    q.append((x, time + n + 1))
            
            # else if no more tasks to process but there are still tasks on cooldown, we update time to next time
            # task can be processed at (slight optmization)
            elif q:
                time = q[0][1] - 1
            
        return time


