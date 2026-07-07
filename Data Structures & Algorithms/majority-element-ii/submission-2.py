class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        limit = len(nums) // 3

        n1 = -1
        n2 = -1
        c1 = 0
        c2 = 0

        for n in nums:
            if n1 == n:
                c1 += 1
            elif n2 == n:
                c2 += 1
            elif c1 == 0:
                n1 = n
                c1 += 1
            elif c2 == 0:
                n2 = n
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1

        c1 = c2 = 0
        for n in nums:
            if n == n1:
                c1 += 1
            if n == n2:
                c2 += 1

        result = []
        if c1 > len(nums) // 3:
            result.append(n1)
        if c2 > len(nums) // 3:
            result.append(n2)

        return result






        