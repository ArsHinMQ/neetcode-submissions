class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)
        total_tasks = len(tasks)
        for t in tasks:
            counter[t] += 1

        heap = []
        for t in counter:
            heapq.heappush(heap, (-counter[t], t))
        
        total_tasks = len(tasks)
        res = 0
        while total_tasks > 0:
            cooldown = []
            for i in range(n+1):
                if total_tasks == 0:
                    break
                if len(heap) > 0:
                    c, t = heapq.heappop(heap)
                    if c < -1:
                        cooldown.append((c+1, t))
                    total_tasks -= 1
                res += 1
            
            for item in cooldown:
                heapq.heappush(heap, item)
        return res

        
        