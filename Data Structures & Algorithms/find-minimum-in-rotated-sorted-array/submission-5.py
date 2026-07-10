class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        res = float('inf')
        while l <= h:
            m = (l + h) // 2
            if nums[l] > nums[h]:
                l = m + 1
            else:
                h = m - 1
                while l > 0 and nums[l] > nums[l-1]:
                    l -= 1
            res = min(nums[m], res)
        return res


        