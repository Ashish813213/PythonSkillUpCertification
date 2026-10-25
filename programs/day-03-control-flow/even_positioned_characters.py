# You are given a String S, you need to print its characters at even
# indices (index starts at 0).


def utility(s):
    for i in range(0, len(s), 2):
        print(s[i], end="")
