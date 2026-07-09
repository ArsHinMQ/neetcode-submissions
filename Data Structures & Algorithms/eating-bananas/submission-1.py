class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        res = high
        res_t = len(piles)

        while low < high:
            mid = (low + high) // 2
            t = 0
            for p in piles:
                t += math.ceil(p / mid)
            if t <= h:
                if t >= res_t:
                    res = mid
                    res_t = t
                high = mid
            else:
                low = mid + 1
        return res
            


        