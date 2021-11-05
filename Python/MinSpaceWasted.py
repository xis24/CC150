from typing import List
import math
import collections


class MinSpaceWasted:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        minTotalBoxSize = math.inf

        for boxSizes in boxes:
            boxSizes.sort()
            if boxSizes[-1] < packages[-1]:
                continue
            # total box size to pack all n packages
            totalBoxSize = 0
            start = 0
            for boxSize in boxSizes:
                # find the largest index of the package which is less or equal to boxSize
                idx = collections.bisect_right(packages, boxSize, start) - 1
                # number of remain packages that this box can be packed.
                packedCount = idx - start + 1
                totalBoxSize += boxSize * packedCount
                start = idx + 1
            minTotalBoxSize = min(minTotalBoxSize, totalBoxSize)

        if minTotalBoxSize == math.inf:
            return -1
        return (minTotalBoxSize - sum(packages)) % 1_000_000_007
