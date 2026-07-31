class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        has_zero = False
        for n in nums:
            if n == 0:
                if has_zero:
                    return [0] * len(nums)
                has_zero = True
                continue
            prod *= n

        res = []
        for n in nums:
            if has_zero:
                if n == 0:
                    res.append(prod)
                else:
                    res.append(0)
                continue
            res.append(prod // n)

        return res
        