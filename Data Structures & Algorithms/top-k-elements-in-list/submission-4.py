class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        bucket = [[] for _ in range(len(nums) + 1)]
        ans = []
        for key in freq:
            bucket[freq[key]].append(key)

        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                while len(ans) < k and bucket[i]:
                    ans.append(bucket[i].pop())

            if len(ans) == k:
                break

        return ans

        
        