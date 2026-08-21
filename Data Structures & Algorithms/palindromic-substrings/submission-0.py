class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def compare(l: int, r: int):
            nonlocal count
            while l < r and l >= 0 and r < len(s):
                if s[l] != s[r]:
                    return
                l -= 1
                r += 1
                count += 1
        for i in range(len(s)):
            count += 1
            compare(i-1, i+1)
            compare(i, i+1)
        return count
        