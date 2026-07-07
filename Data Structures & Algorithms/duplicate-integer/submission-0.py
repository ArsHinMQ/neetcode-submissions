class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        passed = {}
        for n in nums:
            if passed.get(n):
                return True
            passed[n] = True
        return False
        