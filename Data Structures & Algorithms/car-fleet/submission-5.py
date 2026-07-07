class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = [(position[i], speed[i]) for i in range(len(position))]
        combined.sort(reverse=True)

        print(combined)

        fleets = 1
        for i in range(len(combined) - 1):
            d1, s1 = combined[i]
            d2, s2 = combined[i+1]
            if s1 >= s2:
                fleets += 1
                continue

            c1_steps_needed = (target - d1) / s1
            c2_steps_needed = (target - d2) / s2


            if c1_steps_needed < c2_steps_needed:
                fleets += 1
                continue

            combined[i+1] = (d1, s1)

        return fleets
        