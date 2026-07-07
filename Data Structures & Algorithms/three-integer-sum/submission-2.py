class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            for r in range(len(nums) - 1, l, -1):
                if r < (len(nums) - 1) and nums[r] == nums[r+1]:
                    continue
                pair_sum = nums[l] + nums[r]
                needed = 0 - pair_sum

                ml = l + 1
                mr = r
                while ml < mr:
                    m = (ml + mr) // 2
                    if nums[m] == needed:
                        results.append([nums[l], needed, nums[r]])
                        break
                    elif nums[m] > needed:
                        mr = m
                    else:
                        ml = m + 1
        return results


        