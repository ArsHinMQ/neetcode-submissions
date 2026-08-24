class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        dp = {}
        def dfs(i: int = 0, rem: int = target):
            if rem == 0:
                return True
            elif rem < 0:
                return False

            if i >= len(nums):
                return False

            if dp.get((i+1, rem - nums[i])) is None:
                dp[(i+1, rem - nums[i])] = dfs(i+1, rem-nums[i])
            if dp.get((i+1, rem)) is None:
                dp[(i+1, rem)] = dfs(i+1, rem)

            return dp[(i+1, rem - nums[i])] or dp[(i+1, rem)]

        return dfs()

        
        