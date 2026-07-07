class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n < 0:
                # normalize negative numbers
                nums[i] = 0

        for i, n in enumerate(nums):
            if n == 0:
                continue
            index = abs(n) - 1
            if index < 0 or index >= len(nums):
                # out of range
                continue
            
            if nums[index] < 0:
                # already marked
                continue
            if nums[index] == 0:
                # In worst case, the smallest possible int in the array would be len(nums)
                nums[index] = -(len(nums) + 1)
            else:
                nums[index] *= -1

        for i in range(1, len(nums) + 1):
            index = i - 1

            if nums[index] >= 0:
                return i

        return len(nums) + 1


        
        