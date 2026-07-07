class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dicti = defaultdict(int)
        nums = sorted(set(nums))
        max_len = 0
        for n in nums:
            dicti[n] = dicti[n-1] + 1
            max_len = max(max_len, dicti[n])

        return max_len
            
        