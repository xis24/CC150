class TrappingWater:
    # mono stack
    # Time: O(n)
    # Space: O(n)
    def trap(self, height: List[int]) -> int:
        stack = []
        ret = 0

        for idx, h in enumerate(height):
            # can trap water
            while stack and height[stack[-1]] < h:
                top = stack.pop()  # index of current top
                if stack:
                    w = idx - stack[-1] - 1
                    ret += (min(h, height[stack[-1]] - height[top])) * w
                stack.append(idx)
        return ret

    # Time O(n)
    # Space O(1)
    def trap(self, height):
        leftMax = rightMax = 0
        left, right = 0, len(height) - 1
        ret = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if leftMax < rightMax:
                ret += leftMax - height[left]
                left += 1
            else:
                ret += rightMax - height[right]
                right -= 1
        return ret
