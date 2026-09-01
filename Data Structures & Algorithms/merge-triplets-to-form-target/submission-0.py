class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ai, bi, ci = False, False, False
        for i, triple in enumerate(triplets):
            if triple[0] > target[0] or triple[1] > target[1] or triple[2] > target[2]:
                continue

            if triple[0] == target[0]:
                ai = True
            if triple[1] == target[1]:
                bi = True
            if triple[2] == target[2]:
                ci = True
            
            if ai and bi and ci:
                return True
        return False
            
        