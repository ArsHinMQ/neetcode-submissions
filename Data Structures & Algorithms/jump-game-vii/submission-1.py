class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        i = 0
        while i < len(s) - 1:
            ni = i + minJump
            fni = -1
            while ni <= min(i + maxJump, len(s) - 1):
                if s[ni] != "1" and (ni + minJump <= len(s) - 1 or ni == len(s) - 1):
                    fni = ni
                ni += 1
            if fni == -1:
                return False
            i = fni
        return True