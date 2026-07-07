class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti = {}
        for i, n in enumerate(nums):
            searching_for = target - n
            if dicti.get(searching_for) is not None:
                return [dicti[searching_for], i]
            dicti[n] = i

        return []
