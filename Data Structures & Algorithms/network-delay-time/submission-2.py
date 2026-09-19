class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(set)
        for ui, vi, ti in times:
            adj[ui].add((vi, ti))


        visited = set()
        queue = deque([(k, 0)])
        counter = 0
        def add_neighbors(node: int):
            for ngh, t in adj[node]:
                if t == 0:
                    visited.add(ngh)
                    add_neighbors(ngh)
                else:
                    queue.append((ngh, t-1))

        while queue:
            length = len(queue)
            while length > 0:
                node, time = queue.popleft()
                length -= 1
                if node in visited:
                    continue
                if time > 0:
                    queue.append((node, time-1))
                    continue
                visited.add(node)
                add_neighbors(node)
            if len(visited) == n:
                return counter
            counter += 1

        if len(visited) == n:
            return counter
        return -1