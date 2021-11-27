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
