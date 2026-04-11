class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = { '+' , '/', '-' , '*' }
        stack = []
        for i in range (len(tokens)):
            s = tokens[i]
            if s not in operators:
                stack.append(int(s))
                print(stack)
            else:
                b,a = stack.pop(),stack.pop()
                if s == "+":
                    stack.append(a + b)
                elif s == "-":
                    stack.append(a - b)
                elif s == "*":
                    stack.append(a * b)
                elif s == "/":
                    stack.append(int(a / b))
                        
        return (stack[-1])
        