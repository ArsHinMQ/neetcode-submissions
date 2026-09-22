class Solution:
    def reorganizeString(self, s: str) -> str:
        s = sorted(s)
        chars = defaultdict(int)
        for c in s:
            chars[c] += 1

        heap = []
        for c in chars:
            if chars[c] == 0:
                continue
            heapq.heappush(heap, (-chars[c], c))

        waiting = None
        res = ""
        while heap:
            _, c = heapq.heappop(heap)
            chars[c] -= 1
            res += c
            if waiting is not None:
                heapq.heappush(heap, (-chars[waiting], waiting))
                waiting = None
            if chars[c] > 0:
                waiting = c
        return res if len(res) == len(s) else ""
        



        