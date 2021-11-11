import bisect


class BinarySearchReview:

    # find the left most insertion place
    def bisect_left(self, arr, target):
        left = 0
        right = len(arr)

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    # find the right most inserction place

    def bisect_right(self, arr, target):
        left = 0
        right = len(arr)

        while left < right:
            mid = (left + right) // 2
            if target < arr[mid]:
                right = mid
            else:
                left = mid + 1
        return

    def binary_search(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == '__main__':
    arr = [1, 3, 3, 4, 5, 6, 6, 8, 10, 10]
    obj = BinarySearchReview()
    print(obj.bisect_left(arr, 3))  # 1
    print(obj.bisect_left(arr, 4))  # 3
    print(obj.bisect_left(arr, 7))  # 7
    print("right")
    print(obj.bisect_right(arr, 3))  # 3
    print(obj.bisect_right(arr, 6))  # 7
    print(obj.bisect_right(arr, 10))  # 10
    print("binary search")
    print(obj.binary_search(arr, 5))
    print(obj.binary_search(arr, 8))
