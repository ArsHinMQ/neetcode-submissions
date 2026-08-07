class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if m == r or nums[m] < nums[m-1]:
                return nums[m]

            if nums[r] <= nums[m]:
                l = m + 1
            else:
                r = m
    
            

        