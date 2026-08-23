class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i: int = 0, rem: int = target):
            if rem == 0:
                res.append(subset.copy())
                return
            elif rem < 0:
                return
            if i >= len(nums):
                return

            
            subset.append(nums[i])
            dfs(i, rem-nums[i])
            subset.pop()

            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            dfs(j, rem)
        dfs()
        return res
        