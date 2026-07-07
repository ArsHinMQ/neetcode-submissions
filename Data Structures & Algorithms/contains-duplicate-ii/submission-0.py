class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        t = {}
        for i, n in enumerate(nums):
            if t.get(n) is not None:
                j = t.get(n)
                if abs(i - j) <= k:
                    return True
            t[n] = i
        return False
        