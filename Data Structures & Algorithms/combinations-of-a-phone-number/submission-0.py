class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_mapper = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        def dfs(i: int = 0, subset: str = ""):
            if i >= len(digits):
                if subset:
                    res.append(subset)
                return

            d = digits[i]
            for c in digits_mapper[d]:
                dfs(i+1, subset + c)

        dfs()
        return res


        