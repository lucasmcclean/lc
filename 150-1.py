class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for token in tokens:
            match token:
                case "+":
                    stk.append(stk.pop() + stk.pop())
                case "-":
                    lo = stk.pop()
                    stk.append(stk.pop() - lo)
                case "*":
                    stk.append(stk.pop() * stk.pop())
                case "/":
                    lo = stk.pop()
                    stk.append(int(stk.pop() / lo))
                case _:
                    stk.append(int(token))

        return stk.pop()
