class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        l = 0
        res = 0
        for r in range(len(s)):
            c = s[r]
            if table.get(c) is not None and table[c] >= l:
                l = table[c] + 1
            table[c] = r
            res = max(r - l + 1, res)
        return res
                
        