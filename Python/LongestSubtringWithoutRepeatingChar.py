class LongestSubtringWithoutRepeatingCharacters:

    '''
    sliding window

    a b c b c a
          ^
    l             
    0 1 2 3 
        ^
    '''

    def longestSubstring(self, s: str):
        left = right = 0
        char_to_index = {}
        ret = 0
        for right in range(len(s)):
            if s[right] in char_to_index:
                left = max(left, char_to_index[s[right]] + 1)
            char_to_index[s[right]] = right
            ret = max(ret, right - left + 1)
        return ret


if __name__ == '__main__':
    obj = LongestSubtringWithoutRepeatingCharacters()
    print(obj.longestSubstring("abcbca"))
