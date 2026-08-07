class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return True

            if nums[l] == nums[m]:
                l += 1
            elif nums[r] == nums[m]:
                r -= 1
            elif nums[m] > nums[l]:
                # we are in the left side of the array
                if nums[l] <= target < nums[m]:
                    r = m
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m

        if nums[r] == target:
            return True
        return False
        