# Next Permutation - rearrange the array into the lexicographically next greater
# permutation, or into the lowest order if that is not possible.

class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
        left = i + 1
        arr[left:] = arr[left:][::-1]
        return arr
