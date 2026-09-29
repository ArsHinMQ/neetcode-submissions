class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        in_subset = set()
        visited = set()
        def backtrack():
            if len(in_subset) == len(nums):
                res.append(subset.copy()) 
                return 
                           
            for j in range(len(nums)):
                if j in in_subset:
                    continue
                in_subset.add(j)
                subset.append(nums[j])
                if tuple(subset) not in visited:
                    visited.add(tuple(subset))
                    backtrack()
                subset.pop()
                in_subset.remove(j)

        backtrack()
        return res