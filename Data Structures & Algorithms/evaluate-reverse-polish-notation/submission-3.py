class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        d = {'+', '*', '/', '-'}
        stack = []
        value = 0

        for token in tokens:
            if token not in d:
                stack.append(int(token))
            elif token == '+':
                value = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(value))
                value = 0
            elif token == '*':
                value = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(value))
                value = 0
            elif token == '/':
                value = stack[-2] / stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(value))
                value = 0
            else:
                value = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(value))
                value = 0
            print(stack)
        return stack[-1]
            