class DoublyNode:
    def __init__(self,key: int, val: int, prev: "DoublyNode" | None = None, nex: "DoublyNode" | None = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nex = nex


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache: dict[int, DoublyNode] = {}
        self._left: DoublyNode = DoublyNode(0, 0)
        self._right: DoublyNode = DoublyNode(0, 0)
        self._left.nex = self._right
        self._right.prev = self._left

    def _remove_node(self, node: DoublyNode):
        prev, nex = node.prev, node.nex
        prev.nex, nex.prev = nex, prev

    def _insert_node(self, node: DoublyNode):
        prev, nex = self._right.prev, self._right
        prev.nex = nex.prev = node
        node.nex, node.prev = nex, prev

    def get(self, key: int) -> int:
        if self._cache.get(key):
            n = self._cache[key]
            self._remove_node(n)
            self._insert_node(n)
            return n.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self._cache.get(key):
            self._remove_node(self._cache[key])
        node = DoublyNode(key, value)
        self._cache[key] = node
        self._insert_node(node)
        
        if len(self._cache) > self._capacity:
            lru = self._left.nex
            del self._cache[lru.key]
            self._remove_node(lru)
