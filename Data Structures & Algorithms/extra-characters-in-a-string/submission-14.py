class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()
        for w in dictionary:
            node = root
            for c in w:
                if node.children.get(c) is None:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_end = True
        
        dp = {}
        def backtrack(i: int = 0, node: TrieNode = root, count: int = 1):
            if i >= len(s):
                return count - 1

            c = s[i]
            if count == 1 and dp.get(i) is not None:
                return dp[i]

            if c not in node.children:
                res = count + backtrack(i+1, root, 1)
            else:
                node = node.children[c]
                res = min(backtrack(i+1, node, count+1), count + backtrack(i+1, root, 1), backtrack(i+1, root, 1) if node.is_end else float("inf"))
            if count == 1:
                dp[i] = res
            return res
        
        return backtrack()
            
        