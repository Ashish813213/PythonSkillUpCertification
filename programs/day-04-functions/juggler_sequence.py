# Juggler Sequence is a series of integers in which the first term starts
# with a positive integer a and the remaining terms are generated from the
# immediate previous term: a(k+1) = floor(a(k) ** 0.5) if a(k) is even,
# otherwise a(k+1) = floor(a(k) ** 1.5). Find the sequence until it
# becomes 1.

from math import isqrt


class Solution:
    def jugglerSequence(self, n):
        sequence = [n]
        while n != 1:
            n = isqrt(n) if n % 2 == 0 else isqrt(n ** 3)
            sequence.append(n)
        return sequence
