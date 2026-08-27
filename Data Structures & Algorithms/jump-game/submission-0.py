class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        def backtrack(i: int = 0):
            if i >= len(nums) - 1:
                return True
            if nums[i] == 0:
                dp[i] = False
                return dp[i]

            for j in range(nums[i], 0, -1):
                if dp.get(i+j) is None:
                    dp[i+j] = backtrack(i+j)
                if dp[i+j]:
                    return True
            
            return False
        return backtrack()
        
        