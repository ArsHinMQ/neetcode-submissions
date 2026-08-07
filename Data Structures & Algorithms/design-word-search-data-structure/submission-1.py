class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True
        

    def search(self, word: str) -> bool:
        def dfs(word: str, cur: TrieNode):
            if word[0] == ".":
                for child in cur.children:
                    if len(word) == 1:
                        if cur.children[child].is_end:
                            return True
                    elif dfs(word[1:], cur.children[child]):
                        return True
                return False
            elif word[0] in cur.children:
                if len(word) == 1:
                    return cur.children[word[0]].is_end
                return dfs(word[1:], cur.children[word[0]])
            return False
        
        return dfs(word, self.root)
        
