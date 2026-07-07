class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti = {}
        for s in strs:
            in_order = "".join(sorted(s))
            if dicti.get(in_order):
                dicti[in_order].append(s)
            else:
                dicti[in_order] = [s]

        return list(dicti.values())