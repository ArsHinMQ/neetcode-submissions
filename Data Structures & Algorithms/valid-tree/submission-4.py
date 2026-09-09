class Node:
    def __init__(self, val: int):
        self.val = val
        self.linked: Set[int] = set()

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mappings = {}
        for edge in edges:
            parent, child = edge
            if mappings.get(parent) is None:
                mappings[parent] = Node(parent)
            if mappings.get(child) is None:
                mappings[child] = Node(child)
            
            pn, cn = mappings[parent], mappings[child]
            pn.linked.add(cn.val)
            cn.linked.add(pn.val)

        queue = deque()
        visited = set()
        root = None
        for i in range(n):
            if mappings.get(i) is None:
                visited.add(i)
                continue
            node = mappings[i]
            if root is None or len(node.linked) > len(root.linked):
                root = node

        if root is None:
            return True

        queue.append(root)
        visited.add(root.val)

        while queue:
            node = queue.popleft()
            for l in node.linked:
                ln = mappings[l]
                ln.linked.remove(node.val)
                if ln.val in visited:
                    return False
                queue.append(ln)
                visited.add(ln.val)

            
        return len(visited) == n