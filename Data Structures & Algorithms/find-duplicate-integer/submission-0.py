class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m = min(nums)
        i = 0
        while True:
            index = nums[i] - m
            if index == i:
                i += 1
                continue
            if nums[i] == nums[index]:
                return nums[index]
            n = nums[i]
            nums[i] = nums[index]
            nums[index] = n
        return 0


        