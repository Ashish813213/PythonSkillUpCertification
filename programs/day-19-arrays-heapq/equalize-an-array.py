# Equalize an array - min operations to make all elements equal, where each
# operation adds or subtracts k from a single element. Return -1 if impossible.

class Solution:
    def equalizeArray(self, arr, k):
        r = arr[0] % k
        for x in arr:
            if x % k != r:
                return -1
        arr.sort()
        med = arr[len(arr) // 2]
        return sum(abs(x - med) for x in arr) // k
