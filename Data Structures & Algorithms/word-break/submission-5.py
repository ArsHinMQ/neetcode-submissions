class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for w in wordDict:
            node = root
            for c in w:
                if node.children.get(c) is None:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_end = True
        
        dp = {}
        def backtrack(i: int, node: TrieNode, start_idx: int):
            if i >= len(s):
                return True
            
            c = s[i]
            if dp.get((i, start_idx)) is not None:
                return dp[(i, start_idx)]

            if node.children.get(c) is None:
                return False
            
            node = node.children[c]
            if node.is_end:
                dp[(i+1, start_idx)] = backtrack(i+1, node, start_idx)
                dp[(i+1, i+1)] = backtrack(i+1, root, i+1)
                return dp[(i+1, start_idx)] or dp[(i+1, i+1)]
            elif i == len(s) - 1:
                return False
            else:
                dp[(i+1, start_idx)] = backtrack(i+1, node, start_idx)
                return dp[(i+1, start_idx)]
        
        
        return backtrack(0, root, 0)

            
            