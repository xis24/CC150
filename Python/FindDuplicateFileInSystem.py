from typing import List
import collections


class FindDuplicateFileInSystem:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)

        for path in paths:
            directory, *files = path.split()
            for file in files:
                fileName, content = file.split("(")
                groups[content].append(directory + "/" + fileName)

        return [path for path in groups.values() if len(path) > 1]

# follow ups

# 1. Imagine you are given a real file system, how will you search files? DFS or BFS ?
# In general, BFS will use more memory then DFS. However BFS can take advantage of the
# locality of files in inside directories, and therefore will probably be faster

# BFS can take parallelism when try to find
# BFS explores neighbors first. This means that files which are located close to each other are also accessed
# one after another. This is great for space locality and that's why BFS is expected to be faster. Also, BFS is easier to parallelize (more fine-grained locking). DFS will require a lock on the root node.


# 2. If the file content is very large (GB level), how will you modify your solution?
# In a real life solution we will not hash the entire file content, since it's not practical.
# Instead we will first map all the files according to size. Files with different sizes are
# guaranteed to be different. We will than hash a small part of the files with equal sizes
# (using MD5 for example). Only if the md5 is the same, we will compare the files byte by byte
# Both SHA256 and MDA5 are hashing algorithms. They take your input data, in this case your file,
# and output a 256/128-bit number. This number is a checksum.

# 3. If you can only read the file by 1kb each time, how will you modify your solution?
# This won't change the solution. We can create the hash from the 1kb chunks, and then
# read the entire file if a full byte by byte comparison is required.

# What is the time complexity of your modified solution? What is the most time consuming part and memory consuming part of it? How to optimize?
# Time complexity is O(n^2 * k) since in worse case we might need to compare every file to all others. k is the file size
# Comparing the file (by size, by hash and eventually byte by byte) is the most time consuming part.
# Generating hash for every file will be the most memory consuming part.
# We follow the above procedure will optimize it, since we compare files by size first, only when sizes differ, we'll generate and compare hashes, and only when hashes are the same, we'll compare byte by byte.
# Also, using better hashing algorithm will also reduce memory/time.

# How to make sure the duplicated files you find are not false positive?
# We will use several filters to compare: File size, Hash and byte by byte comparisons.
