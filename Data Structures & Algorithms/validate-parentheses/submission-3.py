class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        matches = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []
        for c in s:
            if c in ("(", "{", "["):
                stack.append(c)
            else:
                if not stack or matches[stack[-1]] != c:
                    return False
                stack.pop()

        if len(stack) > 0:
            return False

        return True


        