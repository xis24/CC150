import abc
from abc import ABC, abstractclassmethod
from typing import List


class Node(ABC):
    @abstractclassmethod
    def eval(self) -> int:
        pass


class BinaryNode(Node):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def eval(self) -> int:
        pass


class Num(Node):
    def __init__(self, val) -> None:
        self.value = val

    def eval(self) -> int:
        return int(self.value)


class Plus(BinaryNode):
    def eval(self) -> int:
        return self.left.eval() + self.right.eval()


class Minus(BinaryNode):
    def eval(self) -> int:
        return self.left.eval() - self.right.eval()


class Mul(BinaryNode):
    def eval(self) -> int:
        return self.left.eval() * self.right.eval()


class Div(BinaryNode):
    def eval(self) -> int:
        return self.left.eval() // self.right.eval()


class ExpressionTreeWithEvaluteFunction(object):

    def buildTree(self, postfix: List[str]):
        operators = {
            "+": Plus,
            "-": Minus,
            "*": Mul,
            "/": Div
        }
        stack = []
        for token in postfix:
            if token in operators:
                R = stack.pop()
                L = stack.pop()
                stack.append(operators[token](L, R))
            else:
                stack.append(Num(token))
        return stack[0]


if __name__ == '__main__':
    obj = ExpressionTreeWithEvaluteFunction()
    expTree = obj.buildTree(["3", "4", "+", "2", "*", "7", "/"])
    print(expTree.eval())
