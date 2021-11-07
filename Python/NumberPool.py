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

# #######Frequency of checkout and checkin########


class NumberPool:

    def __init__(self):
        # largest checkout number
        self.mmax_chk_out = 0
        # min heap of numbers that have been checked back in
        self.min_heap = []

    def checkout(self):
        if not self.min_heap:
            self.mmax_chk_out += 1
            return self.mmax_chk_out
        return self.min_heap[0]

    def checkin(self, num):
