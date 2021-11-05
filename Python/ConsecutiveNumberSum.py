class ConsecutiveNumberSum:
    def consecutiveNumbersSum(self, N):
        if N <= 2:
            return 1
        n = N // 2 + 1
        start = 1
        counter = 0
        currentSum = 0

        for end in range(1, n + 1):
            currentSum += end

            while currentSum > N and start <= end:
                currentSum -= start
                start += 1
            if currentSum == N:
                counter += 1
        return counter + 1


if __name__ == '__main__':
    obj = ConsecutiveNumberSum()
    print(obj.consecutiveNumbersSum(15))
    print(obj.consecutiveNumbersSum(9))


# N = 9
# n = 5
# 1 2 3 4 5
#       10 15
# 2 3 4 => counter + 1 = 1
# 4 5 => counter + 1 = 2
# 9 => counter + 1 = 3
