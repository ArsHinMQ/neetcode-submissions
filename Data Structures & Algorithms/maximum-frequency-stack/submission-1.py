class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0
        
    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]
        self.max_freq = max(f, self.max_freq)
        self.group[f].append(val)

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if len(self.group[self.max_freq]) < 1:
            self.max_freq -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()