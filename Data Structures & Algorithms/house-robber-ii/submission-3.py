class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses: List[int]):
            prev, curr = 0, 0
            for h in houses:
                prev, curr = curr, max(curr, prev + h)
            return curr

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))