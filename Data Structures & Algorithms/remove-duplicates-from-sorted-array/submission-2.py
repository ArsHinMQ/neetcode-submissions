class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = -1
        i = 1
        k = 0
        while i < len(nums):
            if nums[i] == nums[k]:
                if l == -1:
                    l = i
            else:
                k += 1
                if l != -1:
                    nums[l], nums[i] = nums[i], nums[l]
                    l += 1
            i += 1
        return k + 1