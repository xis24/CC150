class DecodeWays:

    # Time complexity: O(n)
    # Space complexity: O(n)
    def numDecodings(self, s: str) -> int:
        return self.dfs(s, 0, {})

    def dfs(self, s, index, memo):
        # if you have seen this substring
        if index in memo:
            return memo[index]

        # if you reach the end of the string, return 1 for success
        if index == len(s):
            return 1

        if s[index] == '0':
            return 0

        # there could be two ways to parse it, for last one digit, or last two digit
        if index == len(s) - 1:
            return 1

        ans = self.dfs(s, index + 1, memo)
        if int(s[index:index + 2]) <= 26:
            ans += self.dfs(s, index + 2, memo)
        memo[index] = ans
        return ans

    # iterative ways
    # space O(n)
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 1

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # it's for ease of computations
        dp[1] = 1

        for i in range(1, n):
            if s[i] == '0':
                dp[i + 1] += dp[i]
            twoDigit = int(s[i-1: i + 1])
            if twoDigit >= 10 and twoDigit <= 26:
                dp[i + 1] += dp[i - 1]

        return dp[n]

    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 1
        n = len(s)
        two_back = 1  # two character behind current character
        one_back = 1  # one character behind current character

        for i in range(1, n):
            current = 0
            if s[i] != '0':
                current += one_back
            twoDigit = int(s[i-1: i + 1])
            if twoDigit >= 10 and twoDigit <= 26:
                current += two_back
            two_back = one_back
            one_back = current
        return one_back


if __name__ == '__main__':
    obj = DecodeWays()
    print(obj.numDecodings("1225"))
    # print(obj.numDecodings("226"))
