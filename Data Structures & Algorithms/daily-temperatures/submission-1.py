class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        mapping = {}
        result = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            t = temperatures[i]
            while stack and stack[-1] <= t:
                stack.pop()
            if stack:
                result[i] = mapping[stack[-1]] - i
            stack.append(t)
            mapping[t] = i
        return result

        