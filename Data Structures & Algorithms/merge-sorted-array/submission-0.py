class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[m:] + nums1[:m]
        print(nums1)
        i = len(nums1) - m
        j = 0
        index = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums1[index] = nums1[i]
                nums1[i] = 0
                i += 1
            else:
                nums1[index] = nums2[j]
                nums2[j] = 0
                j += 1
            index += 1

        while j < len(nums2):
            nums1[index] = nums2[j]
            nums2[j] = 0
            j += 1
            index += 1
        print(nums1)

        