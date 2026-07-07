class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        results = []
        nums.sort()
        l, r = 0, len(nums) - 1
        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l-1]:
                continue

            for r in range(len(nums) - 1, -1, -1):
                if r < (len(nums) - 1) and nums[r] == nums[r+1]:
                    continue


                s = nums[l] + nums[r]
                needed = target - s
        
                il, ir = l + 1, r - 1
                while il < ir:
                    if il > (l + 1) and nums[il] == nums[il-1]:
                        il += 1
                        continue
                    if ir < (r - 1) and nums[ir] == nums[ir+1]:
                        ir -= 1
                        continue
                    inner_sum = nums[il] + nums[ir]
                    if inner_sum == needed:
                        results.append([nums[l], nums[il], nums[ir], nums[r]])
                        ir -= 1
                        il += 1
                    elif inner_sum > needed:
                        ir -= 1
                    else:
                        il += 1
            

        return results

                
            

            

        