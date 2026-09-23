class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        last_in_list = None
        lilc = 0
        heap = [(-a, "a"), (-b, "b"), (-c, "c")]
        heapq.heapify(heap)
        res = ""
        while heap:
            count, char = heapq.heappop(heap)
            if count == 0:
                continue
            elif last_in_list == char:
                if lilc == 2:
                    if not heap:
                        break
                    ncount, nchar = heapq.heappop(heap)
                    if ncount == 0:
                        break
                    res += nchar
                    last_in_list = nchar
                    lilc = 1
                    heapq.heappush(heap, (ncount+1, nchar))
                    heapq.heappush(heap, (count, char))
                else:
                    lilc += 1
                    res += char
                    heapq.heappush(heap, (count+1, char))
            else:
                last_in_list = char
                res += char
                lilc = 1
                heapq.heappush(heap, (count+1, char))
        return res

        