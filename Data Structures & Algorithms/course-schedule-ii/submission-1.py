class Node:
    def __init__(self, val: int):
        self.val = val
        self.children = 0
        self.parents: List["Node"] = []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mappings = {}
        for pq in prerequisites:
            after, before = pq
            if mappings.get(before) is None:
                mappings[before] = Node(before)
            if mappings.get(after) is None:
                mappings[after] = Node(after)

            bn, an = mappings[before], mappings[after]
            bn.parents.append(an)
            an.children += 1

        res = []
        visited = set()
        queue = deque()
        for idx in range(numCourses):
            node = mappings.get(idx)
            if node is None:
                res.append(idx)
                continue
            if node.children != 0:
                continue
            queue.append(node)
            visited.add(idx)
            res.append(idx)
        
        while queue:
            node = queue.popleft()
            for parent in node.parents:
                parent.children -= 1
                if parent.children != 0:
                    continue
                if parent.val in visited:
                    continue
                queue.append(parent)
                visited.add(parent.val)
                res.append(parent.val)
        return res if len(res) == numCourses else []
