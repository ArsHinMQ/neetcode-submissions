class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        jumps = 0
        mi = 0  # max index
        mi_candidate = 0
        i = 0
        while i < len(nums) - 1:
            if nums[mi] + mi >= len(nums) - 1:
                jumps += 1
                break
            i += 1
            if i - (nums[mi] + mi) == 0:
                if (nums[mi_candidate] + mi_candidate) - i > nums[i]:
                    mi = mi_candidate
                else:
                    mi = i
                jumps += 1
            elif (nums[mi] + mi) - i < nums[i] and (nums[mi_candidate] + mi_candidate) - i < nums[i]:
                mi_candidate = i
        return jumps
        