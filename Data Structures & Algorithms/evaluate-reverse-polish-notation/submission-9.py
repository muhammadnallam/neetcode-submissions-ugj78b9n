class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            print(stack)
            if t == '+':
                sum = stack.pop() + stack.pop()
                stack.append(sum)
            elif t == '-':
                diff = stack[-2] - stack[-1]
                del stack[-2:]
                stack.append(diff)
            elif t == '*':
                product = stack.pop() * stack.pop()
                stack.append(product)
            elif t == '/':
                quotient = int(stack[-2] / stack[-1])
                del stack[-2:]
                stack.append(quotient)
            else:
                stack.append(int(t))
        
        return stack[0]



        