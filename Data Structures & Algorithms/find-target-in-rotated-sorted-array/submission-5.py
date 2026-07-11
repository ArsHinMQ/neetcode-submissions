class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            if nums[m] > nums[r]:
                # we're in the left portion of the array
                if target > nums[m]:
                    l = m + 1
                else:
                    if nums[l] <= target:
                        r = m - 1
                    else:
                        l = m + 1
            else:
                # we're in the right portion of the array
                if target < nums[m]:
                    r = m - 1
                else:
                    if target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
        return -1

            
        