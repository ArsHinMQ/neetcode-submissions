"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def backtrack(n: Optional['Node']):
            if n is None:
                return
            if n.val in visited:
                return visited[n.val]
            
            cn = Node(n.val)
            visited[n.val] = cn
            for ng in n.neighbors:
                cn.neighbors.append(backtrack(ng))
            return cn
        return backtrack(node)
        