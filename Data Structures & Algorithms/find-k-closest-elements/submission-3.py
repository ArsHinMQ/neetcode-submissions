class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        result = None
        for r in range(len(arr)):
            if r - l < k:
                continue
            if abs(x - arr[l]) <= abs(x - arr[r]):
                if result is not None:
                    rl, rr = result
                    if abs(x - arr[l]) >= abs(x - arr[rl]) or abs(x - arr[r]) >= abs(x - arr[rr]):
                        l += 1
                        continue
                result = (l, r)
            l += 1


        return arr[l:r+1] if result is None else arr[result[0]:result[1]]

        