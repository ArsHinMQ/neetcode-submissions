class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_profit = [(capital[i], profits[i]) for i in range(len(profits))]
        capital_profit.sort()
        heap = []
        l = 0
        while k > 0:
            for i in range(l, len(capital_profit)):
                c, p = capital_profit[i]
                if c > w:
                    break
                heapq.heappush(heap, -p)
                l += 1
            if not heap:
                break
            profit = heapq.heappop(heap)
            w += -profit
            k -= 1
        return w

        