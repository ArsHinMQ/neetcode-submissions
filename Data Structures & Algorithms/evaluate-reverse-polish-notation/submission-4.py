class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if t not in ("+", "-", "*", "/"):
                nums.append(int(t))
                continue

            n1 = nums.pop()
            n2 = nums.pop()
            if t == "+":
                nums.append(n1 + n2)
            if t == "*":
                nums.append(n1 * n2)
            if t == "-":
                nums.append(n2 - n1)
            if t == "/":
                nums.append(int(n2 / n1))

        return nums[-1]
        