class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, f in freq.items():
            bucket[f].append(num)

        result = []
        for i in range(len(bucket) - 1, -1, -1):
            while bucket[i] and len(result) < k:
                result.append(bucket[i].pop())

            if len(result) >= k:
                break

        return result


        
        