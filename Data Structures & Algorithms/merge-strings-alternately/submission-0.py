class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        s = ""
        while i < min(len(word1), len(word2)):
            s += word1[i] + word2[i]
            i += 1

        while i < len(word1):
            s += word1[i]
            i += 1
        while i < len(word2):
            s += word2[i]
            i += 1

        return s


        