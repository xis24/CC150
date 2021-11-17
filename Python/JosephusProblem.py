class JosephusProblem:
    def josephus(self, nums, skip):
        skip -= 1
        idx = skip
        while len(nums) > 1:
            nums.pop(idx)  # kill prisoner at idx
            idx = (idx + skip) % len(nums)
        return nums[0]
