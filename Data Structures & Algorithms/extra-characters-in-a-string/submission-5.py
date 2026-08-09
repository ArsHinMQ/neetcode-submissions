class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end: bool = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()
        for word in dictionary:
            node = root
            for c in word:
                if not node.children.get(c):
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_end = True

        
        dp = [0] * (len(s) + 1)
        for i in range(len(s) - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            node = root
            for j in range(i, len(s)):
                c = s[j]
                if c not in node.children:
                    break
                node = node.children[c]
                if node.is_end:
                    dp[i] = min(dp[i], dp[j+1])
        return dp[0]