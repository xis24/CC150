import random
from typing import List
import collections


# So the problem from Facebook will ask for the index of max number instead of target number.
class RandomPickIndex:
    # brute force
    def __init__(self, nums: List[int]):
        self.nums = nums

    # space O(m), where m is number of target in the array
    # time O(1) + O(n) = O(n) since we need to iterate the whole array to find out number of target
    def pick(self, target: int) -> int:
        index_list = [i for i, num in enumerate(self.nums) if num == target]
        return random.choice(index_list)

    # Caching results using a hashmap
    # Time O(n)
    # space O(n)
    def __init__(self, nums: List[int]):
        self.hashmap = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.hashmap[num].append(i)

    # Time O(1)
    def pick(self, target: int) -> int:
        return random.choice(self.hashmap[target])

    # reservoir sampling
    # since the array size can be large, we need to use reservoir sampling
    # it's also good for streaming process

    '''
    Someone linked to another explanation, which is good, but I'd like to write a relatable one to demonstrate the concept. Imagine you're at one of those restaurants with a rotating sushi conveyor. The sushi chef puts out fish, seaweed, or rice dishes. You only eat fish, but you want to give a fair chance for all the fish dishes you see before you pick one. So, you'll sit there and wait for the entire conveyor belt to go around once; that way you'll have seen what there is before you make your pick. When each dish goes in front of you, you'll ignore it if it's not a fish one. But, if it is a fish one, you're going to look at how many fish dishes you've seen and decide of whether you will pick that one. For example, on the first fish you see, you decide you will definitely pick that one, so you mark that down the dish serial number on your note pad. For the second fish you see, you again decide whether you pick this one or not, but you have to consider that there was a previous one, so you open your phone and go on the web to find a random number generator to pick a number between 1 and 2. If the result is a 1, then you don't have to change your note; if it's a 2, then you erase the dish serial number you wrote down in your note pad and put down this dish's new serial number instead. A few rice dishes come by, oh but now you see a third fish dish! So, you get the random generator out and pick number between 1 and 3. You won't change your note if that generated number isn't a 3. More rice and seaweed dishes come by, and then you reach the end. Gotta wait until the sushi comes back around. So, based on what you've seen so far, there have been 3 fish dishes, and each time you saw a fish dish, you decided whether that is the one you'd pick. Now you just have to wait until that particular fish comes back around! Or, you can just show the dish's serial number to the chef and have him grab that one for you ;)

    This is how reservoir sampling works. At each element, you're deciding if you will pick that one or not based on probability of entire population. If not, then you already chose before, so just go with that one.
    '''

    def __init__(self, nums: List[int]):
        self.num = nums

    # Time O(1)
    def pick(self, target: int) -> int:
        count = 0
        ret = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                count += 1
                chance = random.randint(1, count)
                if chance == count:
                    ret = i
        return ret
