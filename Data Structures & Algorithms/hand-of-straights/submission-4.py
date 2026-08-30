class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        nog = len(hand) // groupSize # Number of Groups
        dic = defaultdict(int)
        nums = set()
        for h in hand:
            dic[h] += 1
            nums.add(h)
        print(dic)
        for _ in range(nog):
            size = groupSize - 1
            last_item = min(nums)
            dic[last_item] -= 1
            if dic[last_item] == 0:
                nums.remove(last_item)
            while size > 0:
                if dic[last_item + 1] == 0:
                    print(last_item)
                    return False
                last_item += 1
                dic[last_item] -= 1
                size -= 1
                if dic[last_item] == 0:
                    nums.remove(last_item)
        return True
            




        