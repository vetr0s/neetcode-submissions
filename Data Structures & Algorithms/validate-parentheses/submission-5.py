class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}
        for ch in s:
            if brackets.get(ch) is not None:
                stack.append(brackets[ch])
            elif ch in brackets.values():
                if len(stack) < 1:
                    return False
                
                cur_char = stack.pop()
                if cur_char != ch:
                    return False
        
        return not stack

        