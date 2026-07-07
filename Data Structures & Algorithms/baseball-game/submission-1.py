class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = 0
        records = []
        for op in operations:                
            if op == '+':
                records.append(records[-1] + records[-2])
                s += records[-1]
            elif op == 'D':
                records.append(records[-1] * 2)
                s += records[-1]
            elif op == 'C':
                s -= records[-1]
                records.pop()
            else:
                n = int(op)
                records.append(n)
                s += n

        return s
                