# Separate even and odd - segregate array so even numbers come first in sorted
# order, followed by odd numbers in sorted order. Modify the array in-place.

class Solution:

    def segregateEvenOdd(self, arr):
        even = sorted(x for x in arr if x % 2 == 0)
        odd = sorted(x for x in arr if x % 2 == 1)
        arr[:] = even + odd
