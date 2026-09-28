class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # A -> 65 and Z -> 90
        def calc(cn: int = columnNumber):
            if cn <= 26:
                return chr(cn+64)
            code = math.floor(cn / 26)
            if code > 26:
                return calc(code) + calc(cn % 26)
            return chr(code+64) + calc(cn % 26)

        return calc()
        