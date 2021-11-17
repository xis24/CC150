class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())

        n = len(unique)

        self.quickselect(n - k, 0, n - 1, count, unique)
        return unique[n - k:]

    def quickselect(self, k, left, right, count, unique):
        if left == right:
            return

        idx = randint(left, right)
        true_idx = self.partition(idx, left, right, count, unique)

        if true_idx == k:
            return
        if k < true_idx:
            self.quickselect(k, left, true_idx, count, unique)
        else:
            self.quickselect(k, true_idx, right, count, unique)

    def partition(self, idx, left, right, count, unique):
        pivot_frequency = count[unique[idx]]
        unique[idx], unique[right] = unique[right], unique[idx]

        store_idx = left

        for i in range(left, right):
            if count[unique[i]] < pivot_frequency:
                unique[i], unique[store_idx] = unique[store_idx], unique[i]
                store_idx += 1

        unique[store_idx], unique[right] = unique[right], unique[store_idx]
        return store_idx
