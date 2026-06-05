class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # init an array representing the nodes current rulers
        parent = [i for i in range(len(edges) + 1)]

        # if the ruler of a node is not itself, we need to find its ruler, then save the ruler for that node
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        for x, y in edges:
            a = find(x)
            b = find(y)

            # if the rulers are the same, means there is a loop
            if a == b:
                return [x, y]

            # since this was a edge, we just say a is now ruled by b
            parent[a] = b
