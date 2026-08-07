class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []

        subset = []
        def dfs(i: int):
            nonlocal subset
            nonlocal res
            if i >= len(nums):
                res.append(subset.copy())
                return

            # include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # not include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res


            
