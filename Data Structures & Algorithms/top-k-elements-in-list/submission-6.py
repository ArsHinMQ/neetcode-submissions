class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for n in counter:
            bucket[counter[n]].append(n)

        result = []
        for i in range(len(bucket) - 1, -1, -1):
            while bucket[i]:
                result.append(bucket[i].pop())
            if len(result) == k:
                break

        return result

        