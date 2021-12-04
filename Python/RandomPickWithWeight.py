from typing import List
import random


class RandomPickWithWeight:

    '''
Explanation of why prefixSum works:

Think that if we had an array [1,2,3,4,3]. Normal random pickIndex would pick any index from 0 to 4 with equal probability. But we want that index=1 is picked by 2/13 probability, index=0 with 1/13 probability and so on. (13 is sum of weights). To ensure that one way to think of it if we make a larger array (of size 13) where the values are the indices such that index i is repeated w[i] times then if we do a normal rand on this array then index 0 to 12 will be picked randomly with equal probability. 13 index array -> [0, 1,1, 2,2,2, 3,3,3,3, 4,4,4]. So there is a 3/13 chance of picking 2 as 2 is repeated thrice in the new array.

Now instead of actually constructing this 13 index array, we just know the range of the index of the 13 index array where value = i. Eg:

for index=0, range is {0,0}
index =1, range of indices of the new array is {1,2}
index=2, range={3,5}
index=3, range ={6,9}
index = 4, range = {10,12}
In other words,

index=0, range is <1
index=1, range is <3
index=2, range is <6
index = 3, range is < 10
index = 4, range is < 13
If you notice the above numbers 1,3,6,10,13 - they are cumulative sum.
The reason this happens is because for every range: right = left + (w[i] - 1) and left is (prev right+1). So if we substitute 2nd equation into 1st. right = (prev right)+w[i]; i.e. keep adding prev sum to current weight.

Thus the prefixSum is able to implement this.

    '''

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        prefix_sum = 0

        for weight in w:
            prefix_sum += weight
            self.prefix_sum.append(prefix_sum)
        self.total_sum = prefix_sum

    # Time: O(n)
    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        for i, x in enumerate(self.prefix_sum):
            if target < x:
                return i

    # Time: O(log n)
    def pickIndex(self) -> int:
        target = self.total_sum * random.random()

        left = 0
        right = len(self.prefix_sum) - 1
        while left < right:
            mid = (left + right) // 2
            if target > self.prefix_sum[mid]:
                left = mid + 1
            else:
                right = mid
        return left
