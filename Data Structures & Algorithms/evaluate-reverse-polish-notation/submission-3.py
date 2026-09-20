class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        opa = []
        for tok in tokens:
            if tok.lstrip('-').isdigit():
                opa.append(int(tok))
                continue
            # Assuming that it has to be operator
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
        return opa[0]