import collections


class Iterator():

    '''
    Interleave 原题： 给一个int[][], 比如    [ [1,2],[4], [6],  [],  [7,8,9], 输出：[1,4,6,7,2,8,9]。面试关提醒这题很简单，快速写完就行了，没有followup。
    Iterator原题，给一个int[], 写个Iterator 来支持HasNext 和GetNext。要求先写interface，在写implementation.
    Iterator 原题follow up，给一个int start，int finish，int step，要求implement 同一个interface。比如start  = 1, finish = 5, step = 2, GetNext() 就会输出1,3,5
    '''

    def __init__(self, input):
        self.input = input
        self.queue = collections.deque([])

    # simple interleave
    # input: [1,2],[4], [6],  [],  [7,8,9]
    # output: [1,4,6,7,2,8,9]
    def interleave(self):
        rows = len(self.input)
        max_cols = max(len(row) for row in self.input)
        ret = []
        for col in range(max_cols):
            for row in range(rows):
                if col >= len(self.input[row]):
                    continue
                ret.append(self.input[row][col])
        return ret

    def init_queue(self):
        for idx, sublist in enumerate(self.input):
            if sublist:
                # row number, current pos of row
                self.queue.append((idx, 0))

    # O(1) time, O(k) space if k is number of inner array
    def next(self):
        if self.queue:
            row, cur_col = self.queue.popleft()
            next_col = cur_col + 1
            if next_col < len(self.input[row]):
                self.queue.append((row, next_col))
            return self.input[row][next_col]
        # raise
        return -1

    def hasNext(self):
        return len(self.queue) > 0


class OddIterator:
    def __init__(self):
        self.odd = 1

    def next(self):
        next_val = self.odd
        self.odd += 2
        return next_val

    def has_next(self):
        return True


class NegationIterator:
    def __init__(self, iterator):
        self.iter = iterator

    # negate
    def next(self):
        return -self.iter.next()

    def hasNext(self):
        return self.iter.hasNext()


class IteratorOfIterator:
    def __init__(self, list_of_iterator) -> None:
        self.iterators = list_of_iterator
        self.queue = collections.deque([])
        for iter in self.iterators:
            # in case there is nothing inside of iterator
            if iter:
                self.queue.append(iter)

    def next(self):
        ret = None
        if self.queue:
            cur_iter = self.queue.popleft()
            if cur_iter.hasNext():
                res = cur_iter.next()
            if cur_iter.hasNext():
                self.queue.append(cur_iter)
            return ret
        return ret

    def hasNext(self):
        return len(self.queue) > 0


class IteratorRange:
    def __init__(self, start, end, step):
        self.end = end
        self.step = step
        self.cur = start

    def next(self):
        if not self.hasNext():
            raise Exception("out of bound")
        val = self.cur
        self.cur += self.step
        return val

    def hasNext(self):
        return self.cur + self.step <= self.end


if __name__ == '__main__':
    obj = Iterator([[1, 2], [6], [], [7, 8, 9]])
    print(obj.interleave())

    range = IteratorRange(1, 5, 2)
    print(range.next())
    print(range.next())
    print(range.next())
    print(range.hasNext())
    print(range.next())
