import collections

# Input: sky is the blue
# Output: blue  the is sky


class ReverseWordsInString:
    def reverseWords(self, s: str) -> str:
        l = self.trim_spaces(s)
        self.reverse(l, 0, len(l) - 1)
        self.reverse_each_word(l)

        return ''.join(l)

    def trim_spaces(self, s):
        left, right = 0, len(s) - 1

        # leading spaces
        while left <= right and s[left] == ' ':
            left += 1

        # trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1

        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':  # skip multiple spaces
                output.append(s[left])
            left += 1

        return output

    def reverse(self, l, left, right):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

    def reverse_each_word(self, l):
        n = len(l)
        start = end = 0

        while start < n:
            while end < n and l[end] != ' ':
                end += 1

            self.reverse(l, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1

# another way is to use deque, and append each word to the left, and join them together in the end
    def reverseWords(self, s: str) -> str:
        left = 0
        right = len(s) - 1

        while left <= right and s[left] == ' ':
            left += 1

        while left <= right and s[right] == ' ':
            right -= 1

        deque = collections.deque([])
        word = []
        while left <= right:
            if s[left] == ' ' and word:
                deque.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        deque.appendleft(''.join(word))
        return ' '.join(deque)
