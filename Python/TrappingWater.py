from typing import List


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
                    # to find out the width we are trying to covering
                    w = idx - stack[-1] - 1
                    # to find out min(h, height[stack[-1]]) height we need to use to take diferrence between current poped height
                    ret += (min(h, height[stack[-1]]) - height[top]) * w
                stack.append(idx)
        return ret

    '''
    Let's assume left,right,leftMax,rightMax are in positions shown in the graph below.

      2       1      3       2
    left_max left right_max right

    we can see height[left] < height[right],then for pointerleft, he knows a taller bar exists on his right side, then if leftMax is taller than him, he can contain some water for sure(in our case). So we go ans += (left_max - height[left]). But if leftMax is shorter than him, then there isn't a left side bar can help him contain water, then he will become other bars' leftMax. so execute (left_max = height[left]).
    Same idea for right part.
    '''
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
