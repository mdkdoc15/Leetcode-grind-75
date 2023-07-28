# Created by matthewkight at 7/28/23
class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                num2 = stack.pop()
                num1 = stack.pop()
                result = 0
                if token == '+':
                    result = num1 + num2
                elif token == '-':
                    result = num1 - num2
                elif token == '*':
                    result = num1 * num2
                else:
                    result = int(num1 / num2)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]

if __name__ == '__main__':
    s= Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(s.evalRPN(tokens))