class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = [(position[i], speed[i]) for i in range(len(position))]
        position_speed.sort()
        stack = []

        for i in range(len(position_speed) - 1):
            stack.append(i)
            while stack:
                j = stack[-1]
                p, s = position_speed[j]
                np, ns = position_speed[i + 1]
                if s <= ns:
                    break

                t = (target - p) / s
                nt = (target - np) / ns
                if t > nt:
                    break
                stack.pop()
        return len(stack) + 1
            
        