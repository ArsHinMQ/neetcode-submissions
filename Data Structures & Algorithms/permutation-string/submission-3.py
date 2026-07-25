class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter = defaultdict(int)
        for c in s1:
            counter[c] += 1

        l = 0
        data = defaultdict(deque)
        for i, c in enumerate(s2):
            if counter[c] == 0:
                data = defaultdict(deque)
                l = i + 1
                continue
            elif len(data[c]) + 1 > counter[c]:
                target_index = data[c][0]
                smallest_index = i - 1
                for j in range(97, 123):
                    tc = chr(j)
                    while data[tc] and data[tc][0] <= target_index:
                        data[tc].popleft()
                    if data[tc]:
                        smallest_index = min(data[tc][0] - 1, smallest_index)
                l = smallest_index + 1

            data[c].append(i)
            if i - l == len(s1) - 1:
                return True
        return False
        