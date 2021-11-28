class IntegerToEnglishWords:

    def __init__(self):
        self.lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six",
                           "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                           "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Fourty",
                     "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        res = ""
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                res = self.helper(num % 1000) + self.thousands[i] + " " + res
            num //= 1000
        return res.strip()

    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.lessThan20[num] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:  # num < 1000
            return self.lessThan20[num // 100] + " Hundred " + self.helper(num % 100)


class RomanToInteger:
    def romanToInt(self, s: str) -> int:
        value_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        index = 0
        ret = 0
        while index < len(s):
            if index + 1 < len(s) and s[index:index + 2] in value_map:
                ret += value_map[s[index:index+2]]
                index += 2
            else:
                ret += value_map[s[index]]
                index += 1
        return ret


class IntegerToRoman:
    def intToRoman(self, num: int) -> str:
        values = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                  (100, 'C'), (90, 'XC'), (50, 'L'),  (40, 'XL'), (10, 'X'),
                  (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        ret = []
        for val, symbol in values:
            count, num = divmod(num, val)
            ret.append(count * symbol)
        return "".join(ret)


if __name__ == '__main__':
    obj = IntegerToEnglishWords()
    print(obj.numberToWords(123450))
