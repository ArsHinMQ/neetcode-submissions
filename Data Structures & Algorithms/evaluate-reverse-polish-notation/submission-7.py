class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                s = stack.pop()
                f = stack.pop()
                stack.append(f - s)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                s = stack.pop()
                f = stack.pop()
                stack.append(math.floor(f/s) if f / s >= 0 else math.ceil(f/s))
            else:
                stack.append(int(t))
        return stack[-1] if stack else 0

        