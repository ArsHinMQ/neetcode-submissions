class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            vl = heights[l]
            vr = heights[r]
            curr_area = min(vl, vr) * (r - l)
            max_area = max(max_area, curr_area)
            if vl < vr:
                l += 1
            else:
                r -= 1

        return max_area
        