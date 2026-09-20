class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+', '-', '*', '/'}
        opa = []
        for tok in tokens:
            if tok in ops:
                right = opa.pop()
                left = opa.pop()
                op = tok
                if op == '+':
                    opa.append(left + right)
                    continue
                elif op == '-':
                    opa.append(left - right)
                    continue
                elif op == '*':
                    opa.append(left * right)
                    continue
                elif op == '/':
                    opa.append(int(left / right))
                    continue
            # Assuming that it has to be operand
            opa.append(int(tok))
            
            
        return opa[0]