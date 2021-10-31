from typing import List


class SearchSuggestionsSystem:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        array_len = len(products)
        ans = []
        input_char = ""

        for char in searchWord:
            tmp = []
            input_char += char
            insertion_index = self.binary_search(products, input_char)
            for word_ind in range(insertion_index, min(array_len, insertion_index + 3)):
                if products[word_ind].startswith(input_char):
                    tmp.append(products[word_ind])
            ans.append(tmp)
        return ans

    def binary_search(self, array, target):
        left = 0
        right = len(array)
        while left < right:
            mid = (left + right) // 2
            if array[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
