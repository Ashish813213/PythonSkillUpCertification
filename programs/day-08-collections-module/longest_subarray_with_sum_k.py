# Find the length of the longest subarray whose elements sum to exactly k.
# Return 0 if no such subarray exists.

class Solution:
    def longestSubarray(self, arr, k):
        seen = {}
        total = 0
        best = 0
        for i, v in enumerate(arr):
            total += v
            if total == k:
                best = i + 1
            if total - k in seen:
                best = max(best, i - seen[total - k])
            if total not in seen:
                seen[total] = i
        return best
