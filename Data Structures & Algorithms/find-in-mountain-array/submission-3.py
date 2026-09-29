class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l = 1
        r = mountainArr.length() - 1
        peak_index = -1
        while True:
            m = (l + r) // 2
            left, mid, right = mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)

            if left < mid > right:
                peak_index = m
                break
            elif mid < right:
                l = m + 1
            else:
                r = m

        if mountainArr.get(peak_index) == target:
            return peak_index
        
        l = 0
        r = peak_index
        while l < r:
            m = (l + r) // 2
            mid = mountainArr.get(m)
            if mid == target:
                return m
            elif mid > target:
                r = m
            else:
                l = m + 1

        l = peak_index + 1
        r = mountainArr.length()
        while l < r:
            m = (l + r) // 2
            mid = mountainArr.get(m)
            if mid == target:
                return m
            elif mid < target:
                r = m
            else:
                l = m + 1
        
        return -1
