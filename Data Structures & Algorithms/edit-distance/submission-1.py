class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mem = {}
        def backtrack(i: int, j: int):
            if j >= len(word2) and i >= len(word1):
                return 0
            elif (i, j) in mem:
                return mem[(i, j)]
            elif j >= len(word2):
                mem[(i, j)] = len(word1) - i
            elif i >= len(word1):
                mem[(i, j)] = len(word2) - j
            elif word1[i] == word2[j]:
                mem[(i, j)] = backtrack(i+1, j+1)
            else:
                mem[(i, j)] = 1 + min(backtrack(i+1, j), backtrack(i, j+1), backtrack(i+1, j+1))
            return mem[(i, j)]
        return backtrack(0, 0)