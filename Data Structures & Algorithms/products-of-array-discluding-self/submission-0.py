class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [0] * len(nums)
        prefix_prod[0] = nums[0]

        suffix_prod = [0] * len(nums)
        suffix_prod[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix_prod[i] = nums[i] * prefix_prod[i-1]

        for i in range(len(nums) - 2, -1, -1):
            suffix_prod[i] = nums[i] * suffix_prod[i+1]
            
        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = (prefix_prod[i-1] if i > 0 else 1) * (suffix_prod[i+1] if i < len(nums) - 1 else 1)

        return result



        