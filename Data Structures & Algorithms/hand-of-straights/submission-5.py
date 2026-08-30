class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        nog = len(hand) // groupSize # Number of Groups
        dic = {}
        for h in hand:
            dic[h] = dic.get(h, 0) + 1

        for _ in range(nog):
            size = groupSize - 1
            last_item = min(dic)
            dic[last_item] -= 1
            if dic[last_item] == 0:
                del dic[last_item]
            while size > 0:
                last_item += 1
                if dic.get(last_item) is None:
                    return False
                dic[last_item] -= 1
                size -= 1
                if dic[last_item] == 0:
                    del dic[last_item]
        return True
            




        