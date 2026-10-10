class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        child_parent = {i: i for i in range(1, n+1)}
        rank = {i: 1 for i in range(1, n+1)}

        def find(node):
            if node == child_parent[node]:
                return node
            child_parent[node] = find(child_parent[node])
            return child_parent[node]

        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                child_parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                child_parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        