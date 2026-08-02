class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            print(t, stack)
            while stack:
                if temperatures[stack[-1]] >= t:
                    break
                j = stack.pop()
                result[j] = i - j
            stack.append(i)
        return result


        