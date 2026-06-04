class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(node, target, visited):
            if node == target:
                return True
            visited.add(node)

            for neigh in graph[node]:
                if neigh not in visited:
                    if dfs(neigh, target, visited):
                        return True
            return False

        for i in range(len(edges)):
            x, y = edges[i]
            if x in graph and y in graph and dfs(x, y, set()):
                return [x, y]
            graph[x].append(y)
            graph[y].append(x)

