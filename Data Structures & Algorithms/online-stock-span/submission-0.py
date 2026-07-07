class StockSpanner:

    def __init__(self):
        self.stack: tuple[int, int] = []
        

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price, 1))
            return 1

        counter = 1
        while self.stack and price >= self.stack[-1][0]:
            counter += self.stack[-1][1]
            self.stack.pop()

        self.stack.append((price, counter))
        return counter

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)