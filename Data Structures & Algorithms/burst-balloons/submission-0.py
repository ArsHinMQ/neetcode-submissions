class Solution:
    def maxCoins(self, nums: List[int]) -> int: 
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l: int, r: int):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            best = 0
            for i in range(l, r+1):
                coins = nums[i] * nums[r+1] * nums[l-1]
                coins += dfs(l, i-1) + dfs(i+1, r)
                best = max(best, coins)
            dp[(l, r)] = best
            return dp[(l, r)]

        return dfs(1, len(nums) - 2)


            

            
             