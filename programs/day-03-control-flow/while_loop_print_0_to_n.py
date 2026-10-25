# Given a number n, print all numbers from 0 to n in increasing order
# in a single line using a while loop.

n = int(input())
i = 0

while i <= n:
    print(i, end="" if i == n else " ")
    i += 1
