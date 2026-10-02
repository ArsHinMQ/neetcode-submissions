class FreqStack:

    def __init__(self):
        self.mapping = defaultdict(int)
        self.heap = []
        self.count = 0
        
    def push(self, val: int) -> None:
        self.mapping[val] += 1
        self.count += 1
        heapq.heappush(self.heap, (-self.mapping[val], -self.count, val))

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.mapping[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()