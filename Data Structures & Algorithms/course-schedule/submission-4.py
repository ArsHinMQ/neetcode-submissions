class Node:
    def __init__(self, val: int, children: Optional[List[Node]] = None, parents: Optional[List[Node]] = None):
        self.val = val
        self.children = children if children is not None else []
        self.parents = parents if parents is not None else []

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
            an.children.append(bn)
            bn.parents.append(an)

        queue = deque()
        counter = 0
        visited = set()
        for idx in range(numCourses):
            if mappings.get(idx) is None:
                visited.add(idx)
                continue
            node = mappings[idx]
            if not node.children:
                queue.append(node)
                visited.add(node.val)

        if not queue:
            return False

        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                for p in node.parents:
                    if p.val in visited:
                        continue
                    is_ready = True
                    for c in p.children:
                        if c.val not in visited:
                            is_ready = False
                            break
                    if is_ready:
                        queue.append(p)
                        visited.add(p.val)
            counter += 1
            if len(visited) == numCourses:
                return True
            if counter > numCourses:
                return False
        return len(visited) == numCourses
            


        