class FindCeleberity:

    ''' 
        definition of celeberity: he knows no one, but everyone knows him
        we need to find out that person. If there is no celeberity, return - 1

        brute force solution is for each person, we call knows api on others, to see
        if other knows this person, and this person doesn't know others.

        This will result a O(n^2) time complexity, with O(1) space
    '''

    # API call
    def knows(self, a, b):
        pass

    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            if self.isCelebertiy(i, n):
                return i

        return -1

    def isCeleberity(self, candidate, n):
        for i in range(n):
            if i == candidate:
                continue

            if self.knows(candidate, i) or not self.know(i, candidate):
                return False
        return True

    '''
    we  can actually simply the process. knows(a, b) == True, it tells us a knows b; a can't be 
    a celeberity. knows(a, b) == False, it tells a doesn't know b, and a could be a celeberity.
    we could just use the first info to get the potential candidate. Then we can iterate the array
    again to check if our candidate is real celeberity

    Time complexity: O(n)
    Space complexity: O(1)
    '''

    def findCelebrity(self, n: int) -> int:
        candidate = 0  # initilize candiate as first person
        for i in range(n):
            if self.knows(candidate, i):
                # i could be potential candidate
                candidate = i

        if self.isCeleberity(candidate, n):
            return candidate
        return -1
