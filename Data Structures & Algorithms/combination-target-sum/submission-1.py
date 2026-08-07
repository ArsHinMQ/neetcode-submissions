class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i: int, total: int = 0):
            if total == target:
                res.append(subset.copy())
                return
            elif total > target:
                return
            if i >= len(nums):
                return

            total += nums[i]
            subset.append(nums[i])
            dfs(i, total)

            total -= subset.pop()    
            dfs(i+1, total)
            

        dfs(0)
        return res
        