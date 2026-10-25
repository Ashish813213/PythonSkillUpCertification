# Given a number n, find the value of n raised to the power of its own
# reverse. The result will always fit into a 32-bit signed integer.


class Solution:
    def reverseExponentiation(self, n):
        reverse = int(str(n)[::-1])
        return n ** reverse
