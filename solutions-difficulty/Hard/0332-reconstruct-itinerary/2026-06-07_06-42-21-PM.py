class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # build adjacenecy list using a min heap as the list of nodes
        graph = collections.defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        out = []
        # post order dfs
        def dfs(airport):
            while graph[airport]:
                dest = heapq.heappop(graph[airport])
                dfs(dest)
            out.append(airport)
        
        dfs("JFK")
        return out[::-1]

