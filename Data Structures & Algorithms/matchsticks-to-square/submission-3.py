class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        length = total // 4
        if max(matchsticks) > length:
            return False

        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def dfs(i: int = 0):
            if i >= len(matchsticks):
                return True

            ms = matchsticks[i]
            for j, side in enumerate(sides):
                if side + ms <= length:
                    sides[j] += ms
                    if dfs(i+1):
                        return True
                    sides[j] -= ms

                if sides[j] == 0:
                    break
            return False
        return dfs()
            
        