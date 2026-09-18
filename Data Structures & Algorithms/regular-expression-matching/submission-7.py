class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def backtrack(i: int, j: int):
            if i < 0 and j < 0:
                return True
            elif i < 0:
                while j >= 0:
                    if p[j] != "*":
                        return False
                    j -= 2
                return True
            elif j < 0:
                return False
            if s[i] == p[j] or p[j] == ".":
                return backtrack(i-1, j-1)
            elif p[j] == "*":
                c = p[j-1]
                while (c == s[i] or c == ".") and i >= 0:
                    if backtrack(i, j-2):
                        return True
                    i -= 1
                return backtrack(i, j-2)
            else:
                return False
            
        return backtrack(len(s) - 1, len(p) - 1)