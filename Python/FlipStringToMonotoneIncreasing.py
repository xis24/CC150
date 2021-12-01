class FlipStringToMonotoneIncreasing:

    '''
    Given a binary string, return the min fliping to make it monotone increasing sequence
    '''

    # what we want is [0] * i + [1] * j
    # for every position, we have to know how many ones we need to flip before, and how many zeros we need to flip after

    def minFlipsMonoIncr(self, s):
        n = len(s)
        count_zeros = s.count('0')
        count_one = 0
        # in the case of all zeros, we need to start with the cost to convert all zeros to ones
        res = n - count_zeros

        for i in range(n):
            if s[i] == '0':
                count_zeros -= 1
            elif s[i] == '1':
                res = min(res, count_one + count_zeros)
                count_one += 1
        return res
