class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        elif nums[0] == 0:
            return False
        i = 1
        mi = 0
        while i < len(nums) - 1:
            if nums[mi] + mi == i:
                if nums[i] == 0:
                    return False
                mi = i
            else:
                mi = mi if (mi + nums[mi]) - i > nums[i] else i
            i += 1
        return True
            
            
        
        