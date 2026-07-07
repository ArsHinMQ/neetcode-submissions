class Solution:

    def merge_sort(self, nums: List[int]):
        if len(nums) == 1:
            return nums

        length = len(nums)
        mid = length // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])

        final = []
        while left and right:
            if left[0] < right[0]:
                final.append(left.pop(0))
            else:
                final.append(right.pop(0))

        final.extend(left)
        final.extend(right)

        return final


    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)
        