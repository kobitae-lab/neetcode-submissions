class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = {'(', '[', '{'}
        closed_brackets = {')', ']', '}'}

        open_stack = []

        for bracket in s:
            if bracket in open_brackets:
                open_stack.append(bracket)
            elif not open_stack:
                return False
            else:
                if open_stack[-1] == '(' and bracket != ')':
                    return False
                elif open_stack[-1] == '[' and bracket != ']':
                    return False
                elif open_stack[-1] == '{' and bracket != '}':
                    return False
                else:
                    open_stack.pop()

        if open_stack:
            return False
        else:
            return True