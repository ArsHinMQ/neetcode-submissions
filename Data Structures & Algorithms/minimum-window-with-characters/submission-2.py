class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = defaultdict(int)
        for c in t:
            t_counter[c] += 1
            t_counter["total"] += 1
            if t_counter[c] == 1:
                t_counter["need"] += 1

        l = 0
        s_counter = defaultdict(int)
        res = ()
        for r, c in enumerate(s):
            if t_counter[c] == 0:
                if s_counter["total"] == 0:
                    l = r
                continue
            else:
                s_counter[c] += 1
                s_counter["total"] += 1
                if s_counter[c] == t_counter[c]:
                    s_counter["have"] += 1

            while s_counter["have"] == t_counter["need"]:
                res = (l, r+1) if not res or res[1] - res[0] > (r+1) - l else res

                lc = s[l]
                if t_counter[lc] == 0:
                    l += 1
                    continue
                s_counter[lc] -= 1
                s_counter["total"] -= 1
                l += 1
                if s_counter[lc] < t_counter[lc]:
                    s_counter["have"] -= 1
            

        return s[res[0]:res[1]] if res else ""

        
                
        