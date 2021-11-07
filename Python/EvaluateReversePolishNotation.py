from typing import List


class EvaluateReversePolishNotation:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a/b)
        }

        stack = []
        for token in tokens:
            if token in operations:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(operations[token](num1, num2))
            else:
                stack.append(int(token))
        return stack[0]


if __name__ == '__main__':
    obj = EvaluateReversePolishNotation()
    print(obj.evalRPN(["2", "1", "/", "3", "+"]))
