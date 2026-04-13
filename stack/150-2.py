class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            match token:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    x = stack.pop()
                    stack.append(stack.pop() - x)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    x = stack.pop()
                    stack.append(int(stack.pop() / x))
                case _:
                    stack.append(int(token))

        return stack.pop()
