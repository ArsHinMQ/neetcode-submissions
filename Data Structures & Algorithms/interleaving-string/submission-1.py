class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        def backtrack(i: int, j: int, sub: str):  
            if (i, j) in dp:
                return dp[(i, j)]          
            if sub != s3[:len(sub)]:
                dp[(i, j)] = False
            elif i >= len(s1) and j >= len(s2):
                if sub == s3:
                    dp[(i, j)] = True
                else:
                    dp[(i, j)] = False
            elif j >= len(s2):
                dp[(i, j)] = backtrack(i+1, j, sub+s1[i])
            elif i >= len(s1):
                dp[(i, j)] = backtrack(i, j+1, sub+s2[j])
            else:
                dp[(i, j)] = backtrack(i+1, j, sub+s1[i]) or backtrack(i, j+1, sub+s2[j])
            return dp[(i, j)]

        return backtrack(0, 0, "")
        