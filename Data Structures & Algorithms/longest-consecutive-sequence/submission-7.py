class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = set()
        for n in nums:
            table.add(n)

        if not table:
            return 0

        res = 1
        for n in table:
            if n - 1 not in table:
                length = 1
                while n + 1 in table:
                    length += 1
                    res = max(length, res)
                    n = n + 1
        return res
        
        
        