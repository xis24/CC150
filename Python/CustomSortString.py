import collections


class CustomSortString:
    def customSortString(self, order: str, s: str) -> str:
        count = collections.Counter(s)
        ans = []

        for c in order:
            if c in count:
                ans.append(c * count.pop(c))

        for c, v in count.items():
            ans.append(c * v)

        return "".join(ans)

    # Relative Sort Array
    # arr2 unique order, arr1 has all elements
    # requirement append the result based on the order; if element is not in the sequence,
    # append those elements in ascending order

    def relativeSortArray(self, arr1, arr2):
        count = collections.Counter(arr1)
        ans = []

        for num in arr1:
            if count[num]:
                ans.append([num] * count.pop(num))

        for i in range(1001):
            if count[i]:
                ans.append([i] * count[i])
        return ans


if __name__ == '__main__':
    obj = CustomSortString()
    print(obj.customSortString("cba", "abcd"))
