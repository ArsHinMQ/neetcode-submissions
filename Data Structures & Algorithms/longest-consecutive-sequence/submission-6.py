class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = set()
        for n in nums:
            table.add(n)

        if not table:
            return 0

        res = 1
        count = 1
        mini = min(table)
        table.remove(mini)
        while table:
            if mini + 1 in table:
                count += 1
                table.remove(mini+1)
                mini = mini + 1
                continue
            res = max(count, res)
            count = 1
            mini = min(table)
            table.remove(mini)
        return max(count, res)
        
        
        