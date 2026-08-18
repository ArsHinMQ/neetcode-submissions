class Solution:
    def longestPalindrome(self, s: str) -> str:
        def calc_diff(r1: Tuple[int, int], r2: Tuple[int, int]):
            d1, d2 = r1[1] - r1[0], r2[1] - r2[0]
            if d2 > d1:
                return r2
            return r1
        res = (0, 0)
        for i in range(0, len(s)):
            l = (i - 1 if i > 0 else 0) if len(s) % 2 != 0 else i
            r = i + 1 if i < len(s) - 1 else i

            if s[l] != s[r]:
                if s[l] == s[i]:
                    l -= 1
                    res = calc_diff(res, (l+1, i))
                elif s[r] == s[i]:
                    r += 1
                    res = calc_diff(res, (i, r-1))
            
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                res = calc_diff(res, (l, r))
                l -= 1
                r += 1
                

        return s[res[0]:res[1]+1]
        