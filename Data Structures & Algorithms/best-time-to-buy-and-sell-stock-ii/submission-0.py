class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bc = prices[0]
        sc = prices[0]
        total = 0
        for p in prices[1:]:
            # print(p, bc, sc)
            if sc > p:
                total += sc - bc
                bc, sc = p, p
            else:
                sc = p

        total += sc - bc

        return total
        