class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # num = [(index, start left, end right, found smaller, found bigger, result)]
        stack = [(0, heights[0])]
        max_h = 0
        for i in range(1, len(heights)):
            index = i
            while stack and stack[-1][1] > heights[i]:
                prev_index, prev_h = stack.pop()
                max_h = max(max_h, (prev_h * (i - prev_index)))
                index = prev_index
            stack.append((index, heights[i]))
        
        max_index = len(heights)
        for i, h in stack:
            max_h = max(max_h, (h * (max_index - i)))
        return max_h


            






        