class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok not in ["+", "-", "*", "/"]:
                stack.append(tok)
            else: # must be an operator
                op2 = int(stack.pop())
                op1 = int(stack.pop())

                if tok == "+":
                    stack.append(op1 + op2)
                elif tok == "-":
                    stack.append(op1 - op2)
                elif tok == "*":
                    stack.append(op1 * op2)
                elif tok == "/":
                    stack.append(op1 / op2)

        return int(stack[-1])
            
            