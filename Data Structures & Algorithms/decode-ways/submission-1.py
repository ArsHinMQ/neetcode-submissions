class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def decode(i: int = 0, attach: bool = False):
            if i == len(s):
                if attach:
                    return 0
                return 1
            if dp.get((i, attach)) is not None:
                return dp[(i, attach)]
            n = s[i]
            count = 0
            if attach:
                if s[i-1] == "2" and n not in {"0", "1", "2", "3", "4", "5", "6"}:
                    count = 0
                else:
                    count += decode(i+1, False) 
            else:
                if n == "1" or n == "2":
                    count += decode(i+1, False)
                    count += decode(i+1, True)
                elif n == "0":
                    count = 0
                else:
                    count += decode(i+1, False)
            dp[(i, attach)] = count
            return count
        r = decode()
        return r
            
        