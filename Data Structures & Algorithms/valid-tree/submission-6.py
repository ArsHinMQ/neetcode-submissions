class Node:
    def __init__(self, val: int):
        self.val = val
        self.linked: List[int] = []

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        visited = set([0])
        queue = deque([0])

        while queue:
            node = queue.popleft()
            for ngh in adj[node]:
                if ngh in visited:
                    continue
                visited.add(ngh)
                queue.append(ngh)

        return len(visited) == n 
