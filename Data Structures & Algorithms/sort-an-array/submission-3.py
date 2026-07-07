class Solution:

    def merge_sort(self, nums: List[int]):
        if len(nums) == 1:
            return nums

        length = len(nums)
        mid = length // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])

        final = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                final.append(left[i])
                i += 1
            else:
                final.append(right[j])
                j += 1

        final.extend(left[i:])
        final.extend(right[j:])

        return final


    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)
        