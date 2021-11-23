class MinRemoveToMakeValidParentheses:

    '''
    Given a string s of (, ) and lowercase english characters.
    Remove min number of parentheses to make string valid. And Return that string
    '''

    # 1. We use stack to save the index of (, whenver we see a ), we check
    #   a. if stack is empty, this is invalid index. We add this index to a set
    #   b. if stack is not empty, we pop the element in stack to match ).
    # 2. Then we pop all elements (index of unmatched "(" to the set)
    # 3. construct the answer based on the set

    # Time O(n)
    # Space O(n)
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  # save ( index
        delete_index = set()
        for idx, char in enumerate(s):
            if char == '(':
                stack.append(idx)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    delete_index.add(idx)
        ret = []
        for idx, char in enumerate(s):
            if idx in delete_index:
                continue
            ret.append(char)
        return ''.join(stack)


class MinNumberOfSwapToMakeStringBalanced:
    '''
    You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

    A string is called balanced if and only if:

    It is the empty string, or
    It can be written as AB, where both A and B are balanced strings, or
    It can be written as [C], where C is a balanced string.
    You may swap the brackets at any two indices any number of times.

    Return the minimum number of swaps to make s balanced.

    Input: s = "]]][[["
    Output: 2
    Explanation: You can do the following to make the string balanced:
    - Swap index 0 with index 4. s = "[]][][".
    - Swap index 1 with index 5. s = "[[][]]".
    The resulting string is "[[][]]".

    '''

    # First cancel out all the valid pairs, then you will be left with something like]]][[[, and
    # the answer will be ceil(m/2). Where m is the number of pairs left.
    def minSwaps(self, s: str) -> int:
        balance = 0
        max_balance = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                balance = 1
            max_balance = max(max_balance, balance)
        return (max_balance + 1) // 2
