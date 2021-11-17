class Calculator:
    def calculate(self, s: str) -> int:
        return self.calc(s, 0)

    def calc(self, s, index):
        num = 0
        stack = []
        sign = "+"

        while index < len(s):
            if s[index].isdigit():
                num = num * 10 + int(s[index])
            elif s[index] in "+-*/":
                self.update(sign, num, stack)
                num, sign = 0, s[index]  # reset num and update the sign
            elif s[index] == "(":
                num, j = self.calc(s, index + 1)
                index = j - 1
            elif s[index] == ")":
                self.update(sign, num, stack)
                return sum(stack), index + 1
            index += 1
        self.update(sign, num, stack)
        return sum(stack)

    def update(self, op, num, stack):
        if op == "+":
            stack.append(num)
        elif op == "-":
            stack.append(-num)
        elif op == "*":
            stack.append(stack.pop() * num)
        elif op == "/":
            stack.append(stack.pop() / num)


if __name__ == '__main__':
    obj = Calculator()
    # print(obj.calculate("(1+(4+5+2)-3)+(6+8)"))
    print(obj.calculate("5+4*5/3"))
