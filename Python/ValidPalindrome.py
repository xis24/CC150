class ValidPalindrome:

    '''
    string could contain 
    '''

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    '''
    delete at most one char to see if it's a palindrome
    '''

    def isPalindrome2(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != right:
                return self.isValid(s, left, right - 1) and self.isValid(s, left + 1, right)
            left += 1
            right -= 1
        return True

    def isValid(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
