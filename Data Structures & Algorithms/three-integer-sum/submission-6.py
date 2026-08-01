class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        if nums[-1] < 0:
            return []

        results = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            elif i > 0 and nums[i-1] == n:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = n + nums[l] + nums[r]
                if s == 0:
                    results.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        return results
            

            

            
        