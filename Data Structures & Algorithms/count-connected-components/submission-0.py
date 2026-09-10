class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        visited = set()
        counter = 0
        for i in range(n):
            if i in visited:
                continue
            visited.add(i)
            queue = deque([i])
            counter += 1
            while queue:
                node = queue.popleft()
                for ngh in adj[node]:
                    if ngh in visited:
                        continue
                    visited.add(ngh)
                    queue.append(ngh)
        return counter