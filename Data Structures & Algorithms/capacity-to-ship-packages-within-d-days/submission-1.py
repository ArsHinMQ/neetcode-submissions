class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        h = l * len(weights)
        res = 0
        while l <= h:
            m = (l + h) // 2

            capacity = 0
            days_counter = 0
            for w in weights:
                if capacity + w > m:
                    days_counter += 1
                    capacity = 0
                capacity += w
            if capacity:
                days_counter += 1
            
            if days_counter > days:
                l = m + 1
            else:
                res = m
                h = m - 1
        return res
            


        