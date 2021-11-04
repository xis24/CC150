class DivideTwoIntegers:

    # The key observation to make is that the problems are occurring because
    # there are more negative signed 32-bit integers than there are positive
    # signed 32-bit integers. Each positive signed 32-bit integer has a corresponding
    # negative signed 32-bit integer. However, the same is not true for negative
    # signed 32-bit integers. The smallest one, -2147483648, is alone.
    # It is this number that causes the problems.

    # The best solution is to work with negative, instead of positive, numbers.
    # This is allows us to use the largest possible range of numbers, and it covers
    # all the ones we need.

    # At the start of the algorithm, we'll instead convert both inputs to negative.
    # Then, we'll need to modify the loop so that it subtracts the negative divisor
    # from the negative dividend. At the end, we'll need to convert the result back
    # to a positive if the number of negative signs in the input was not 1.

    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend

        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        quotient = 0
        while dividend - divisor <= 0:
            quotient -= 1
            dividend -= divisor

        return -quotient if negatives != 1 else quotient

    def divide(self, dividend: int, divisor: int) -> int:
        # Constants.
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # We need to convert both numbers to negatives.
        # Also, we count the number of negatives signs.
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        quotient = 0
        while divisor >= dividend:
            powerOfTwo = -1
            value = divisor

            while value >= HALF_MIN_INT and value + value >= dividend:
                value += value
                powerOfTwo += powerOfTwo
            quotient += powerOfTwo
            dividend -= value
        return -quotient if negatives != 1 else quotient
