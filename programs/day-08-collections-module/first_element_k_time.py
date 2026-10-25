# Return the first element of arr that appears at least k times.
# If no element reaches k occurrences, return -1.

class Solution:
    def firstElementKTime(self, arr: list[int], k: int) -> int:
        count = {}
        for x in arr:
            count[x] = count.get(x, 0) + 1
            if count[x] == k:
                return x
        return -1
