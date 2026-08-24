class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        subset = set()

        def dfs(i: int = 0, rem: int = target):
            if rem == 0:
                return True
            elif rem < 0:
                return False
            if i >= len(nums):
                return False
            
            subset.add(i)
            if dfs(i+1, rem - nums[i]):
                return True
            subset.remove(i)

            return dfs(i+1, rem)

        return dfs()

        
        