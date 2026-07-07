class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        going_left: list[int] = []
        going_right: list[int] = []

        survival = []

        for a in asteroids:
            if a < 0:
                going_left.append(a)
            else:
                going_right.append(a)

            while going_left and going_right:
                l = going_left.pop()
                r = going_right.pop()
                s = l + r

                if s < 0:
                    going_left.append(l)
                elif s > 0:
                    going_right.append(r)

            if going_left and not going_right:
                survival.extend(going_left)
                going_left = []

        survival.extend(going_left or going_right)
        return survival
                
        