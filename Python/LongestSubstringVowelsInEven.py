class LongestSubstringVowelsInEven:

    # find the longest substring containing vowels in even counts
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {
            'a': 1,
            'e': 2,
            'i': 4,
            'o': 8,
            'u': 16
        }
        # d: last seen index for vowel sequence count map
        d = {0: -1}
        bit_representation_for_vowel_count = 0
        result = 0

        for i, c in enumerate(s):
            if c in vowels:
                bit_representation_for_vowel_count ^= vowels[c]

            # any combination of vowels that gives odd count & have not been seen before
            if bit_representation_for_vowel_count not in d:
                # "stores the oldest index for which a particular combination of vowels resulted into odd count"
                d[bit_representation_for_vowel_count] = i
            else:
                # "if a combination is seen again, result = current_index - last_seen_index_for_this_combination (d[n])"
                # "example: s = "aepqraeae" (odd vowel count for s[:2] is seen again at s[0:]"
                # "not considering character at last seen index will make count even"
                result = max(result, i - d[bit_representation_for_vowel_count])
        return result
