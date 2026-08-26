class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []
        def dfs(i: int = 0, rem: int = target):
            if rem == 0:
                res.append(subset.copy())
                return
            elif rem < 0:
                return
            if i >= len(candidates):
                return

            subset.append(candidates[i])
            dfs(i+1, rem-candidates[i])
            subset.pop()

            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, rem)
        dfs()
        return res


        