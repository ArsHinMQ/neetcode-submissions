class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        res = r
        while l <= r:
            m = (l+r) // 2
            t = 0
            for p in piles:
                t += math.ceil(p / m)
            if t > h:
                l = m + 1
            else:
                res = min(res, m)
                r = m - 1
        return res
        