class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            print(nums[i])

            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s == 0:
                    results.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l <= r:
                        l += 1
                    while nums[r] == nums[r+1] and l <= r:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
            
        return results