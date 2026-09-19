class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(')')
            elif ch == '{':
                stack.append('}')
            elif ch == '[':
                stack.append(']')

            if ch == ')' or ch == '}' or ch == ']':
                if len(stack) < 1:
                    return False

                cur_char = stack.pop()
                if cur_char != ch:
                    return False
        
        if len(stack) > 0:
            return False
        return True

        