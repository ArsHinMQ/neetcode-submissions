class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, x):
        self.freq[x] += 1
        f = self.freq[x]
        if f > self.max_freq:
            self.max_freq = f
        if (f - 1) != 0:
            self.group[f-1].remove(x)
        self.group[f].append(x)

    def pop(self):
        n = self.group[self.max_freq].pop()
        while not self.group.get(self.max_freq) and self.max_freq > 0:
            self.max_freq -= 1

        return n

        

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        stack = FreqStack()

        for n in nums:
            stack.push(n)

        ans = []
        for _ in range(k):
            ans.append(stack.pop())

        return ans
        