class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [1] * len(nums)
        prefix = [1] * len(nums)
        suffix[-1] = nums[-1]
        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]

        res = [suffix[1]]
        for i in range(1, len(nums) - 1):
            res.append(prefix[i-1] * suffix[i+1])
        res.append(prefix[-2])
        return res


        