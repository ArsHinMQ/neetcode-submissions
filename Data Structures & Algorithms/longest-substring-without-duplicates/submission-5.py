class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        t = {}
        l = 0
        r = 0
        longest = 0
        for r, c in enumerate(s):
            if t.get(c) is not None and t[c] >= l:
                longest = max(longest, r - l)
                l = t[c] + 1
                t[c] = r
            else:
                t[c] = r
                longest = max(longest, (r + 1) - l)
        return longest
        