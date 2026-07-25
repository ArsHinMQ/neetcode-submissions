class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = defaultdict(int)
        s2_count = defaultdict(int)
        matches = 0
        for i, c in enumerate(s1):
            s1_count[c] += 1
            s2_count[s2[i]] += 1

        for o in range(97, 123):
            c = chr(o)
            if s1_count[c] == s2_count[c]:
                matches += 1


        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            l = r - len(s1)
            s2_count[s2[l]] -= 1
            s2_count[s2[r]] += 1
            if s2[l] == s2[r]:
                continue
            if s1_count[s2[l]] == s2_count[s2[l]] + 1:
                matches -= 1
            elif s1_count[s2[l]] == s2_count[s2[l]]:
                matches += 1

            if s1_count[s2[r]] == s2_count[s2[r]] - 1:
                matches -= 1
            elif s1_count[s2[r]] == s2_count[s2[r]]:
                matches += 1

        if matches == 26:
            return True

        return False
            



        