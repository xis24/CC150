class WildcardMatching:

    '''
    Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).
    The matching should cover the entire input string (not partial).
    '''

    def isMatch(self, s: str, p: str) -> bool:
        s_cur = 0
        p_cur = 0
        match = 0
        star = -1

        while s_cur < len(s):
            if p_cur < len(p) and (s[s_cur] == p[p_cur] or p[p_cur] == '?'):
                s_cur += 1
                p_cur += 1
            elif p_cur < len(p) and p[p_cur] == '*':
                match = s_cur
                star = p_cur
                p_cur += 1
            elif star != -1:  # we had a * in the pattern
                p_cur = star + 1
                match += 1
                s_cur = match
            else:
                return False

        while p_cur < len(p) and p[p_cur] == '*':
            p_cur += 1

        return p_cur == len(p)  # Check if we have reached the end

# a b e d
#       ^
# ? b * d * *
#         ^
# match 2
# star 2


if __name__ == '__main__':
    obj = WildcardMatching()
    print(obj.isMatch('abed', '?b*d**'))
    # it's easy to see match is moving step by step to almost the end, each time we move 'match', we wil go through the whole
    # tail of p (after *), until we found out b is not a match
    # worst case O(N*M)
    print(obj.isMatch('aaaaaaaaaaaaa', '*aaaaaaab'))
