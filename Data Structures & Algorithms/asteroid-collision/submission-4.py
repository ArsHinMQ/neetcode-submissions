class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                # a is nageative and an asteroid is moving to right
                diff = a + stack[-1]
                if diff < 0:
                    # left won
                    stack.pop()
                elif diff > 0:
                    # right won
                    a = 0
                else:
                    # equal, both lose
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack
                
        