class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        l = 0
        res = 0
        for r in range(len(s)):
            c = s[r]
            if table.get(c) is not None:
                index = table[c]
                for j in range(l, index + 1):
                    table[s[j]] = None
                l = index + 1
            table[c] = r
            res = max(r - l + 1, res)
        return res
                
        