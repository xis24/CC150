class Sort:
    def sortMapBasedOnKey(self):
        map = {
            'b': 10,
            'a': 9,
            'c': 1,
            'd': 3,
            'e': 5,
            'z': 4,
            'u': 4
        }
        print(sorted(map.items(), key=lambda x: x[0]))
        return print(sorted(map.items(), key=lambda x: x[1]))

    def sortListWithMultipleItem(self):
        list = [
            ['a', 1, 150],
            ['z', 10, 20],
            ['u', 200, 5],
            ['a', 20, 100],
        ]

        return print(sorted(list, key=lambda x: (x[0], -x[2])))


if __name__ == '__main__':
    obj = Sort()
    print('map sorting')
    obj.sortMapBasedOnKey()
    print('list sorting')
    obj.sortListWithMultipleItem()
