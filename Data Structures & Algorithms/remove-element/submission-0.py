class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for n in nums.copy():
            if n == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
        