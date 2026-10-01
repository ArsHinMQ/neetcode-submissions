class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        def give_candies(i: int):
            if i >= len(ratings):
                return
                
            pr, pc = (ratings[i-1], candies[i-1]) if i > 0 else (0, 0)
            nr, nc = (ratings[i+1], candies[i+1]) if i + 1 < len(ratings) else (0, 0)
            cr = ratings[i]

            if cr > nr and nc >= candies[i]:
                give_candies(i+1)
                nr, nc = (ratings[i+1], candies[i+1]) if i + 1 < len(ratings) else (0, 0)

            if cr > pr and cr > nr:
                candies[i] = max(nc, pc) + 1
            elif cr > pr:
                candies[i] = pc + 1
            elif cr > nr:
                candies[i] = nc + 1


        for i in range(len(ratings)):
            give_candies(i)

        return sum(candies)

