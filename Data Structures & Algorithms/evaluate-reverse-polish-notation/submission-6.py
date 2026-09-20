class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+', '-', '*', '/'}
        opa = []
        for tok in tokens:
            if tok in ops:
                right = opa.pop()
                left = opa.pop()
                if tok == '+':
                    opa.append(left + right)
                elif tok == '-':
                    opa.append(left - right)
                elif tok == '*':
                    opa.append(left * right)
                elif tok == '/':
                    opa.append(int(left / right))
            else:
                opa.append(int(tok))
        return opa[0]