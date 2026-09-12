class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        self.median = 0

    def addNum(self, num: int) -> None:
        if num > self.median:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        
        while abs(len(self.left) - len(self.right)) > 1:
            if len(self.right) > len(self.left):
                r = heapq.heappop(self.right)
                heapq.heappush(self.left, -r)
            else:
                l = heapq.heappop(self.left)
                heapq.heappush(self.right, -l)
        
        if (len(self.left) + len(self.right)) % 2 != 0:
            self.median = -self.left[0] if len(self.left) > len(self.right) else self.right[0]
        else:
            self.median = (-self.left[0] + self.right[0]) / 2
            
    def findMedian(self) -> float:
        return self.median
        