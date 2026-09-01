class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {c: i for i, c in enumerate(s)}

        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, last_index[c])

            if end == i:
                res.append(size)
                size = 0
        return res
                

        