class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                print(token)
                op2 = stack.pop()
                op1 = stack.pop()

                if token == "+":
                    val = op1 + op2
                    stack.append(val)
                elif token == "-":
                    val = op1 - op2
                    stack.append(val)
                elif token == "*":
                    val = op1 * op2
                    stack.append(val)
                elif token == "/":
                    val = int(op1 / op2)
                    stack.append(val)
                print(stack)
            else:
                stack.append(int(token))
                print(stack)
        
        return int(stack[-1])
            