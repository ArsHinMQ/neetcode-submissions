class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = (0, 0)
        def calc_diff(r1: Tuple[int, int], r2: Tuple[int, int]):
            d1, d2 = r1[1] - r1[0], r2[1] - r2[0]
            if d2 > d1:
                return r2
            return r1

        def compare(l: int, r: int):
            nonlocal res
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                res = calc_diff(res, (l, r))
                l -= 1
                r += 1

        for i in range(0, len(s)):
            compare(i-1, i+1)
            compare(i, i+1)
                

        return s[res[0]:res[1]+1]
        