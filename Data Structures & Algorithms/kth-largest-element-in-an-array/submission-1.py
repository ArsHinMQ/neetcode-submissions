class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ki = len(nums) - k

        def quick_select(l: int = 0, r: int = len(nums) - 1):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] > pivot:
                    continue
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
            
            nums[p], nums[r] = pivot, nums[p]

            if ki == p:
                return pivot
            elif p > ki:
                return quick_select(l, p-1)
            else:
                return quick_select(p+1, r)
        
        return quick_select()

         
        