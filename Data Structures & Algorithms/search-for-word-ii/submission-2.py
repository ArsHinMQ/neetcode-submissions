class TrieNode:
    def __init__(self, val: str):
        self.children = {}
        self.val = val
        self.is_end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode("")
        found = set()

        for word in words:
            node = root
            for c in word:
                if node.children.get(c) is None:
                    node.children[c] = TrieNode(c)
                node = node.children[c]
            node.is_end = True

        visited = set()
        def backtracking(node: TrieNode, r: int, c: int, word: str):
            if node.is_end:
                found.add(word)

            for op in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                dr, dc = op
                nr, nc = r + dr, c + dc
                if nr >= len(board) or nc >= len(board[0]) or nr < 0 or nc < 0:
                    continue
                if (nr, nc) in visited:
                    continue
                letter = board[nr][nc]
                if letter not in node.children:
                    continue
                visited.add((nr, nc))
                backtracking(node.children[letter], nr, nc, word+letter)
                visited.remove((nr, nc))

        def clean_root(node: TrieNode):
            has_end = node.is_end
            for child in list(node.children):
                if clean_root(node.children[child]):
                    has_end = True
                    continue
                del node.children[child]
            return has_end

        for r in range(len(board)):
            for c in range(len(board[0])):
                for letter in list(root.children):
                    node = root.children[letter]
                    if node.val != board[r][c]:
                        continue
                    len_before = len(found)
                    visited = set([(r, c)])
                    backtracking(node, r, c, letter)
                    if len_before < len(found):
                        if clean_root(node):
                           continue
                        del root.children[letter] 

        return list(found)