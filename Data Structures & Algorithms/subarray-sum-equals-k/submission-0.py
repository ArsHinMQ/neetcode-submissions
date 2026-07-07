class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        dicti = defaultdict(int)
        dicti[0] = 1
        counter = 0

        for n in nums:
            prefix += n
            counter += dicti[prefix - k]
            dicti[prefix] += 1

        return counter
        