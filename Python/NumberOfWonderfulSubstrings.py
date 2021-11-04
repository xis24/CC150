class NumberOfWonderfulSubstrings:

    # a wonderful string is a string where at most one letter appears an odd number of times

    def wonderfulSubstrings(self, word: str) -> int:
        # count is a bitmask where each bit represent the count of a character from a-j % 2
        # bitmask is 10 bits, each bit 2 values, 2^10 = 1024
        count = [0] * 1024
        count[0] = 1
        ans = 0
        cur = 0

        for char in word:
            # bitmask of current string ending in char
            cur ^= 1 << (ord(char) - ord('a'))
            # add all even case to result
            ans += count[cur]

            # flip each bit and see if there's matching prefix
            # this adds the 'at most one' odd case
            for i in range(10):
                new_bitmask = cur ^ (1 << i)
                if count[new_bitmask] > 0:
                    ans += count[new_bitmask]
            count[cur] += 1
        return ans
