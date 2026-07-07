class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        max_prefix = 0
        for i, h, in enumerate(height):
            if h >= max_prefix:
                max_prefix = h
                continue
            prefix[i] = max_prefix - h

        suffix = [0] * len(height)
        max_suffix = 0
        for i in range(len(height) - 1, -1, -1):
            h = height[i]
            if h >= max_suffix:
                max_suffix = h
                continue
            suffix[i] = max_suffix - h

        total = 0
        for i in range(len(height)):
            total += min(suffix[i], prefix[i])

        return total
            