class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1
        while True:
            a = (l + r) // 2
            b = half - a - 2  # Off by one error for 0-indexed arrays

            Aleft = A[a] if a >= 0 else float("-infinity")
            Aright = A[a + 1] if a + 1 < len(A) else float("infinity")

            Bleft = B[b] if b >= 0 else float("-infinity")
            Bright = B[b + 1] if b + 1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                r = a - 1
            else:
                l = a + 1
            
