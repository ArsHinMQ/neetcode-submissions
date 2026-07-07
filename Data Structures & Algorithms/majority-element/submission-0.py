class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        majority = len(nums) // 2
        for n in nums:
            cnt[n] += 1
            if cnt[n] > majority:
                return n

        return 0

        