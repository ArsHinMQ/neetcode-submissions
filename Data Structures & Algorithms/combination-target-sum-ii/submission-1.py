class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        subset = []
        total = 0
        def dfs(i: int):
            nonlocal total
            if total == target:
                result.append(subset.copy())
                return
            elif total > target:
                return
            if i >= len(candidates):
                return

            subset.append(candidates[i])
            total += candidates[i]
            dfs(i+1)
            total -= subset.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1)
        dfs(0)
        return result
        