class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # build adjacenecy list using a min heap for lexical order
        graph = collections.defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        out = []

        # post order dfs
        # go all the way to the final airport (the airport with no outward edges)
        # append that and work your way back up the other airports
        def dfs(airport):
            while graph[airport]:
                dest = heapq.heappop(graph[airport])
                dfs(dest)
            out.append(airport)
        
        dfs("JFK")
        # reverse output since list since we are building from the final airport to the start airport
        return out[::-1]

