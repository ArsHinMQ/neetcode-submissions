class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs:
            if len(s) < len(prefix):
                prefix = prefix[:len(s)]
            
            for i in range(len(prefix) - 1, -1, -1):
                if prefix[i] != s[i]:
                    prefix = prefix[:i]

            if not prefix:
                return ""

        return prefix
        