class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        l = 0
        res = 0
        for r, c in enumerate(s):
            while counter[c] > 0:
                counter[s[l]] -= 1
                l += 1
            counter[c] += 1
            res = max(res, r-l+1)
        return res
        