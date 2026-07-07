class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        result = 1
        for i, n in enumerate(nums):
            if n < 0:
                nums[i] = 0

        for n in nums:
            mark = abs(n) - 1
            if mark < 0 or mark >= len(nums):
                # out of bound
                continue
            if nums[mark] < 0:
                # already negative/marked
                continue
            if nums[mark] == 0:
                nums[mark] = -(len(nums) + 1)
                continue
            nums[mark] = -(nums[mark])

        for i in range(1, len(nums) + 1):
            mark = i - 1
            if nums[mark] < 0:
                continue
            return i
        return len(nums) + 1

        
        