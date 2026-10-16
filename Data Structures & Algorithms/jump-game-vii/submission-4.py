class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False

        queue = deque([0])
        farthest = 0
        while queue:
            i = queue.popleft()
            for j in range(max(i+minJump, farthest), min(i+maxJump+1, len(s))):
                farthest = j
                if s[j] == "1":
                    continue
                queue.append(j)
        return farthest == len(s) - 1
                
