class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = set()
        for n in nums:
            table.add(n)

        starters = set()
        for n in nums:
            if (n-1) in table:
                continue
            starters.add(n)

        res = 0
        for n in starters:
            s = n
            count = 1
            while s + 1 in table:
                count += 1
                s += 1
            res = max(count, res)

        return res

        
        