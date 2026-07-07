class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        hashes = defaultdict(int)

        for l in range(len(nums)):
            for r in range(len(nums) - 1, l, -1):
                pair_sum = nums[l] + nums[r]
                needed = 0 - pair_sum
                if hashes.get(f"{nums[l]}-{needed}-{nums[r]}"):
                    continue

                ml = l + 1
                mr = r
                while ml < mr:
                    m = (ml + mr) // 2
                    if nums[m] == needed:
                        results.append([nums[l], needed, nums[r]])
                        hashes[f"{nums[l]}-{needed}-{nums[r]}"] += 1
                        break
                    elif nums[m] > needed:
                        mr = m
                    else:
                        ml = m + 1
        return results


        