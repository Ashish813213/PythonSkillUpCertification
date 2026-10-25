# Find the maximum sum of any contiguous subarray (at least one element)
# of the given integer array.


class Solution:
    def maxSubarraySum(self, arr):
        best = cur = arr[0]
        for x in arr[1:]:
            cur = max(x, cur + x)
            best = max(best, cur)
        return best
