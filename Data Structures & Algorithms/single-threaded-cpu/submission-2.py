class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        mappings = defaultdict(list)
        start_times = set()
        for i, (te, tp) in enumerate(tasks):
            mappings[te].append((tp, i))
            start_times.add(te)

        start_times = list(start_times)
        heapq.heapify(start_times)

        t = start_times[0]
        result = []
        heap = []
        while len(result) != len(tasks):
            while start_times and start_times[0] <= t:
                te = heapq.heappop(start_times)
                for tp, i in mappings[te]:
                    heapq.heappush(heap, (tp, i))
            if not heap:
                t = start_times[0]
                continue
            tp, i = heapq.heappop(heap)
            result.append(i)
            t += tp

        return result

        

        
        