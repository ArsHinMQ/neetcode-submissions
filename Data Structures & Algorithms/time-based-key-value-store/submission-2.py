class TimeMap:

    def __init__(self):
        self.mapping = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        lst = self.mapping[key]
        if not lst:
            return ""

        l = 0
        r = len(lst)
        res = ""
        while l < r:
            m = (l + r) // 2
            t, v = lst[m]
            if t == timestamp:
                return v
            elif t < timestamp:
                res = v
                l = m + 1
            else:
                r = m
        
        return res
        
