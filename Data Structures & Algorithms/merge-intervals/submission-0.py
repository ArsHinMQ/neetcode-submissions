class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort()

        result = [intervals[0]]
        for i in range(1, len(intervals)):
            cs, ce = intervals[i]
            bs, be = result[-1]

            if cs == bs or be >= cs:
                result[-1] = [min(cs, bs), max(ce, be)]
            else:
                result.append(intervals[i])

        return result