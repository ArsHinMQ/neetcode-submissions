class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r = k
        heap = []
        dic = defaultdict(int)
        for n in nums[:r]:
            heap.append(-n)
            dic[n] += 1
        heapq.heapify(heap)

        res = []
        while r < len(nums):
            while dic[-heap[0]] == 0:
                heapq.heappop(heap)
            res.append(-heap[0])
            l = r - k
            dic[nums[l]] -= 1
            r += 1
            dic[nums[r-1]] += 1
            heapq.heappush(heap, -nums[r-1])
        while dic[-heap[0]] == 0:
            heapq.heappop(heap)
        res.append(-heap[0])
        return res
        