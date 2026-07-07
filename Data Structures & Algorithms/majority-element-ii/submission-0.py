class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        limit = len(nums) // 3
        results = set()
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
            if counts[n] > limit:
                results.add(n)
            if len(results) == 3:
                break

        return list(results)


        