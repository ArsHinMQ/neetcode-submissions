class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        banned = set()
        while True:
            fr = 0
            fd = 0
            for i, s in enumerate(senate):
                if i in banned:
                    continue
                if s == "R":
                    fr = min(fr, i)
                    for j in range(max(fd, i+1), len(senate)):
                        if senate[j] == "R" or j in banned:
                            continue 
                        banned.add(j)
                        fd = j + 1
                        break
                    else:
                        fd = 0
                        for j in range(max(fd, i+1)):
                            if senate[j] == "R" or j in banned:
                                continue 
                            banned.add(j)
                            fd = j + 1
                            break
                        else:
                            return "Radiant"
                else:
                    fd = min(fr, i)
                    for j in range(max(fr, i+1), len(senate)):
                        if senate[j] == "D" or j in banned:
                            continue 
                        banned.add(j)
                        break
                    else:
                        for j in range(max(fr, i+1)):
                            if senate[j] == "D" or j in banned:
                                continue 
                            banned.add(j)
                            fr = j + 1
                            break
                        else:
                            return "Dire"
        