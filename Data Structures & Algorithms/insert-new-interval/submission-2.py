class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for i in range(len(intervals) - 1, -1, -1):
            if newInterval[0] >= intervals[i][0]:
                intervals.insert(i+1, newInterval)
                break
        else:
            intervals.insert(0, newInterval)

        result = [intervals[0]]
        i = 1
        while i < len(intervals):
            cs, ce = result[-1]
            ns, ne = intervals[i]
            if ns <= ce or ne <= ce:
                result[-1] = [min(cs, ns), max(ce, ne)]
            else:
                result.append([ns, ne])
            i += 1
        return result


            
        