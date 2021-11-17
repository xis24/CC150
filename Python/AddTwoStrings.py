import collections
from typing import List


class AddTwoStrings:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = collections.deque([])
        index1 = len(num1) - 1
        index2 = len(num2) - 1
        carry = 0

        while index1 >= 0 or index2 >= 2 or carry > 0:
            if index1 >= 0:
                carry += ord(num1[index1]) - ord('0')
                index1 -= 1

            if index2 >= 0:
                carry += ord(num2[index2]) - ord('0')
                index2 -= 1

            ans.appendleft(chr(carry % 10 + ord('0')))
            carry //= 10

        return "".join(ans)


class AddOne:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        return [1] + digits


class AddBinary:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)

        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]  # since bin result starts with 0b


class MultiplyTwoNumbers:
    def multiply(self, num1, num2):
        len1 = len(num1)
        len2 = len(num2)
        ret = [0] * (len1 + len2)

        for i in reversed(range(len1)):
            for j in reversed(range(len2)):
                ret[i + j + 1] += int(num1[i]) * int(num2[j])
                ret[i + j] += ret[i + j + 1] // 10
                ret[i + j + 1] %= 10
        i = 0
        while i < len(ret) and ret[i] == 0:
            i += 1
        res = "".join([str(s) for s in ret[i:]])
        return res if res else '0'


if __name__ == '__main__':
    obj = AddTwoStrings()
    print(obj.addStrings("1158", "472"))
    # obj2 = AddBinary()
    # print(obj2.addBinary("5", "4"))
    obj3 = MultiplyTwoNumbers()
    print(obj3.multiply("123", "24"))
