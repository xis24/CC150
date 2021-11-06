# NumberPool
# Create a number pool, 1 to inifinity which has 2 methods
# checkIn(some_number) and checkout()

# checkout should give the min number checked in
# checkin should add to numberPool if number doesn't exisit

# intially all numbers 1 to inifinity are available

# eg.
# checkout gives 1
# checkout gives 2
# checkin(1)
# checkout gives 1 now

class NumberPool:

    def __init__(self):
        # largest checkout number
        self.mmax_chk_out = 1
        # min heap of numbers that have been checked back in
        self.min_heap = []

    def checkout(self):

    def checkin(self, num):
