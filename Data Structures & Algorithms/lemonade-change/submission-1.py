class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        tenth = 0
        fifth = 0
        for b in bills:
            if b == 5:
                fifth += 1
            elif b == 10:
                if fifth == 0:
                    return False
                fifth -= 1
                tenth += 1
            elif b == 20:
                if tenth >= 1 and fifth >= 1:
                    fifth -= 1
                    tenth -= 1
                elif fifth >= 3:
                    fifth -= 3
                else:
                    return False
        return True
        