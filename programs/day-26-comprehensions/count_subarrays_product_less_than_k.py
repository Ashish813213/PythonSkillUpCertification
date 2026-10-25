# Count the contiguous subarrays whose product is strictly less than k.
# All values are positive, so a sliding window over the product works.

class Solution:
    def countSubarray(self, arr, k):
        prod = 1
        left = count = 0
        for right, x in enumerate(arr):
            prod *= x
            while prod >= k and left <= right:
                prod //= arr[left]
                left += 1
            count += right - left + 1
        return count
