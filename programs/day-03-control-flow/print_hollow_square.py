# Given an integer n, print the hollow square pattern of size n
# using '*' character.


class Solution:
    def printHollowSquare(self, n):
        edge = " ".join("*" for _ in range(n))
        middle = " ".join(["*"] + [" "] * (n - 2) + ["*"])

        for i in range(n):
            print(edge if i == 0 or i == n - 1 else middle)
