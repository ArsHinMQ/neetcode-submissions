class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = "("
        def dfs(i: int = 1, j: int = 0):
            nonlocal subset
            print(subset, i, j)
            if j == n:
                res.append(subset)
                return
            elif i == n:
                subset += ")"
                dfs(i, j+1)
                subset = subset[:len(subset)-1]
                return
            
            subset += "("
            dfs(i+1, j)
            subset = subset[:len(subset)-1]

            if j < i:
                subset += ")"
                dfs(i, j+1)
                subset = subset[:len(subset)-1]

        dfs()
        return res