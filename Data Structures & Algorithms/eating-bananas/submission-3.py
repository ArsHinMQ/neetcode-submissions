class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l < r:
            k = (l + r) // 2
            t = h
            for p in piles:
                t -= math.ceil(p / k)
            if t < 0:
                l = k + 1
            else:
                res = min(res, k)
                r = k
        return res
        