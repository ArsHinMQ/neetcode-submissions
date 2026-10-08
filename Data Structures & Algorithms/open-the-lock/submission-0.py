class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def children(lock: str):
            res = []
            for i in range(4):
                d1 = str((int(lock[i]) + 1) % 10)
                l1 = lock[:i] + d1 + lock[i+1:]
                res.append(l1)

                d2 = str((int(lock[i]) - 1 + 10) % 10)
                l2 = lock[:i] + d2 + lock[i+1:]
                res.append(l2)
            return res

        q = deque()
        q.append(("0000", 0))
        visited = set(deadends)
        while q:
            current, turns = q.popleft()
            if current == target:
                return turns

            for child in children(current):
                if child in visited:
                    continue
                q.append([child, turns+1])
                visited.add(child)
        return -1



            
            


        