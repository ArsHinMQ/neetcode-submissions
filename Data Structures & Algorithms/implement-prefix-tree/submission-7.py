class TrieNode():
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end: bool = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if node.children.get(c) is None:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if node.children.get(c) is None:
                return False
            node = node.children[c]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if node.children.get(c) is None:
                return False
            node = node.children[c]
        return True 
        