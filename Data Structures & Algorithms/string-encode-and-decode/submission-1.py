class Solution:
    splitter = "|#|"

    def encode(self, strs: List[str]) -> str:
        encoded = self.splitter
        for s in strs:
            encoded += s + self.splitter
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == self.splitter:
            return []
        return s.split(self.splitter)[1:-1]
