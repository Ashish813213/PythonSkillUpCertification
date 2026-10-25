# Find all elements of arr that appear more than floor(n/3) times.
# Return them in strictly increasing order, or [] if none exist.

from collections import Counter


class Solution:
    def findMajority(self, arr):
        limit = len(arr) // 3
        return sorted([x for x, c in Counter(arr).items() if c > limit])
