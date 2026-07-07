class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        curr_weight = 0
        carrying = 0
        counter = 0
        while l <= r:
            if carrying == 2:
                counter += 1
                curr_weight = 0
                carrying = 0
                continue

            if curr_weight + people[r] <= limit:
                curr_weight += people[r]
                r -= 1
                carrying += 1
            elif curr_weight + people[l] <= limit:
                curr_weight += people[l]
                l += 1
                carrying += 1
            else:
                counter += 1
                curr_weight = 0
                carrying = 0

        if curr_weight:
            counter += 1

        return counter

            

        