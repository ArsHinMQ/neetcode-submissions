class Solution:
    def checkValidString(self, s: str) -> bool:
        lstack = []
        sstack = []
        for i, c in enumerate(s):
            if c == "(":
                lstack.append(i)
            elif c == "*":
                sstack.append(i)
            else:
                if lstack:
                    lstack.pop()
                elif sstack:
                    sstack.pop()
                else:
                    return False

        if len(lstack) > len(sstack):
            return False

        while lstack:
            if lstack.pop() > sstack.pop():
                return False
        
        return True