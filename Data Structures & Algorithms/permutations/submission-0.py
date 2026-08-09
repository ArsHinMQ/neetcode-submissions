class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(excludes: Set[int]):
            if len(excludes) == len(nums):
                res.append(subset.copy())
                return
            for j in range(len(nums)):
                if j in excludes:
                    continue
                excludes.add(j)
                subset.append(nums[j])
                dfs(excludes)
                subset.pop()
                excludes.remove(j)
        dfs(set())
        return res
        
        