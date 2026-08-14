class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_neg = [-n for n in nums]
        heapq.heapify(nums_neg)

        while k > 1:
            heapq.heappop(nums_neg)
            k -= 1
        return -nums_neg[0]
        