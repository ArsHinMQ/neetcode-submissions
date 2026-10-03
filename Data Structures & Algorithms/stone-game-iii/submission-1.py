class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        def get_val(i: int):
            if i >= len(stoneValue):
                return 0
            return stoneValue[i]

        dp = {}
        def play(i: int = 0, total: int = 0):
            if (i, total) in dp:
                return dp[(i, total)]
            if i >= len(stoneValue):
                return 0, -1

            s1v, s1i = play(i+3)
            s1n, _ = play(s1i) if s1i > i else (0, 0)
            s1 = get_val(i) + get_val(i+1) + get_val(i+2) + s1n

            s2v, s2i = play(i+2)
            s2n, _ = play(s2i) if s2i > i else (0, 0)
            s2 = get_val(i) + get_val(i+1) + s2n

            s3v, s3i = play(i+1)
            s3n, _ = play(s3i) if s3i > i else (0, 0)
            s3 = get_val(i) + s3n

            maxi = max(s1, s2, s3)
            if maxi == s1:
                dp[(i, total)] = total + s1, i+3
            elif maxi == s2:
                dp[(i, total)] = total + s2, i+2
            else:
                dp[(i, total)] = total + s3, i+1

            return dp[(i, total)]

        total_sum = sum(stoneValue)
        alice_total, _ = play()
        bob_total = total_sum - alice_total
        print(alice_total, bob_total)
        if alice_total > bob_total:
            return "Alice"
        elif alice_total == bob_total:
            return "Tie"
        return "Bob"



        