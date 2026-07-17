class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        res = r
        while l <= r:
            m = (l + r) // 2
            count = 0
            total = 0
            for n in nums:
                if total + n > m:
                    total = n
                    count += 1
                    continue
                total += n
            if total:
                count += 1
            
            if count > k:
                l = m + 1
            else:
                res = m
                r = m - 1

        return res


        