class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges) + 1)]

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        for x, y in edges:
            a = find(x)
            b = find(y)

            if a == b:
                return [x, y]
                            
            parent[a] = b
