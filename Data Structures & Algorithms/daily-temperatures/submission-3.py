class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack:
                if temperatures[stack[-1]] >= t:
                    break
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res
                

