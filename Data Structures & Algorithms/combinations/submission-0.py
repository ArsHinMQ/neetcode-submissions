class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i = 1):
            if len(subset) == k:
                res.append(subset.copy())
                return
            elif i > n:
                return
            
            subset.append(i)
            dfs(i+1)
            subset.pop()

            dfs(i+1)

        dfs()
        return res

            
        