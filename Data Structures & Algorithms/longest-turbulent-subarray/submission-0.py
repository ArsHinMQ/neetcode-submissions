class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        cur_len = 1
        max_len = 1

        prev = -1 # -1 = any, 0 = smaller, 1 = greater
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                cur_len = 1
                prev = -1
            elif arr[i] > arr[i - 1]:
                if prev != 1:
                    prev = 1
                    cur_len += 1
                else:
                    cur_len = 2
            elif arr[i] < arr[i-1]:
                if prev != 0:
                    prev = 0
                    cur_len += 1
                else:
                    cur_len = 2
            max_len = max(cur_len, max_len)
        return max_len
        