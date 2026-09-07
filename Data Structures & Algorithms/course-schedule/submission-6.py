class Node:
    def __init__(self, val: int, children: int = 0, parents: Optional[List[Node]] = None):
        self.val = val
        self.parents = parents if parents is not None else []
        self.children = 0
    


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        mappings = {}
        for pq in prerequisites:
            after, before = pq

            if mappings.get(after) is None:
                mappings[after] = Node(after)
            if mappings.get(before) is None:
                mappings[before] = Node(before)

            an, bn = mappings[after], mappings[before]
            an.children += 1
            bn.parents.append(an)

        queue = deque()
        counter = 0
        visited = set()
        for idx in range(numCourses):
            if mappings.get(idx) is None:
                visited.add(idx)
                continue
            node = mappings[idx]
            if node.children == 0:
                queue.append(node)
                visited.add(node.val)
                for p in node.parents:
                    p.children -= 1

        if not queue:
            return False

        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                for p in node.parents:
                    if p.val in visited:
                        continue
                    if p.children != 0:
                        continue
                    queue.append(p)
                    visited.add(p.val)
                    for p2 in p.parents:
                        p2.children -= 1
            counter += 1
            if len(visited) == numCourses:
                return True
            if counter > numCourses:
                return False
        return len(visited) == numCourses
            


        