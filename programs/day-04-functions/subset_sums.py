# Given an array arr of integers, return the sums of all subsets in the
# list. Return the sums in any order.


class Solution:
    def subsetSums(self, arr):
        sums = [0]
        for value in arr:
            sums += [total + value for total in sums]
        return sums
