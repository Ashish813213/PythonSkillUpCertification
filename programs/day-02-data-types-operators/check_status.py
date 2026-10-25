# Given two integers a and b, and an integer flag which is either 0 or 1,
# return true if either of the following conditions is satisfied:
#   1. Exactly one of a or b is non-negative and flag is 0.
#   2. Both a and b are negative and flag is 1.
# Otherwise, return false.


class Solution:
    def checkStatus(self, a: int, b: int, flag: int) -> bool:
        one_non_negative = (a >= 0) != (b >= 0)
        if flag == 0 and one_non_negative:
            return True
        if flag == 1 and a < 0 and b < 0:
            return True
        return False
