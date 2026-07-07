class Solution:
    def decodeSubString(self, s: str, start: int):
        n_str = s[start]
        i = start + 1
        while s[i].isnumeric():
            n_str += s[i]
            i += 1
        n = int(n_str)

        chars = ""
        while i < len(s):
            if s[i] == "]":
                break
            elif s[i].isalpha():
                chars += s[i]
            elif s[i].isnumeric():
                sub_chars, i = self.decodeSubString(s, i)
                chars += sub_chars
            i += 1
        
        return chars * n, i
        

    def decodeString(self, s: str) -> str:
        decoded = ""
        i = 0
        while i < len(s):
            if s[i].isalpha():
                decoded += s[i]
            elif s[i].isnumeric():
                sub_decoded, i = self.decodeSubString(s, i)
                decoded += sub_decoded
            i += 1
        return decoded

        