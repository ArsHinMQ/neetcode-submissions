class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        half = (total + 1) // 2
        
        dp = {}
        def backtrack(i: int = 0, cur_total: int = 0):
            if i >= len(stones) or cur_total >= half:
                return abs(cur_total - (total - cur_total))
            if (i, cur_total) not in dp:
                dp[(i, cur_total)] = min(backtrack(i+1, cur_total + stones[i]), backtrack(i+1, cur_total))

            return dp[(i, cur_total)]
        return backtrack()

