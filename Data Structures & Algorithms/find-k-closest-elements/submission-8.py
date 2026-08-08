class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def diff(i: int):
            return abs(x - arr[i])
        best_r = k - 1
        total_diff = sum([diff(i) for i in range(best_r + 1)])
        for r in range(k, len(arr)):
            rl, rr = best_r - k + 1, best_r
            l = r - k + 1 
            rl_diff = diff(rl)
            r_diff = diff(r)
            if total_diff - rl_diff + r_diff < total_diff:
                best_r = r


        return arr[best_r-k+1:best_r+1]

        