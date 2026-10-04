class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        def play(i: int = 0, m: int = 1):
            if (i, m) in dp:
                return dp[(i, m)]
            if i >= len(piles):
                return -1, 0, m

            max_total = 0
            max_total_idx = i+1
            max_total_m = 1
            ntotal = 0
            limit = m*2
            for j in range(i, min(i+limit, len(piles))):
                ntotal += piles[j]
                nm = max(j-i+1, m)
                bindex, _, bm = play(j+1, nm)
                atotal = 0
                if bindex > j:
                    _, atotal, _ = play(bindex, bm)

                total = ntotal + atotal
                if total > max_total:
                    max_total = total
                    max_total_idx = j+1
                    max_total_m = nm

            dp[(i, m)] = (max_total_idx, max_total, max_total_m)

            return dp[(i, m)]

        _, res, _ = play()
        return res

            
