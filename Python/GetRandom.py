from collections import defaultdict


class GetRandom:
    def __init__(self):
        self.hashmap = defaultdict(set)
        self.list = []

    def insert(self, val: int) -> bool:
        self.hashmap[val].add(len(self.list))
        self.list.append(val)
        return len(self.hashmap[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.hashmap[val]:
            return False
        index = self.hashmap[val].pop()
        lastElement = self.list[-1]
        self.list[index] = lastElement
        self.hashmap[lastElement].add(index)
        self.hashmap[lastElement].discard(len(self.list) - 1)

        self.list.pop()
        return True


if __name__ == '__main__':
    obj = GetRandom()
    print(obj.insert(0))
    # print(obj.remove(0))
    print(obj.insert(0))
    print(obj.insert(1))
    print(obj.remove(0))
