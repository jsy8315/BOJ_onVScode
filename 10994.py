#백준 10994

import sys

N = int(sys.stdin.readline())

if N == 1:
    print("*")

else:
    for i in range(1, 8 * N - 7):
        if i == 2 * N - 1   # 가운데 줄
            print("* " * (2 * N - 2) + "*")
        if (i % 2 == 1) and (i != 2 * N - 1):  # i = 1, 3, 5, 7
            side = "* "
            middle = "*" * (4 * (N - ))
            print(side + middle + side + "*")
        if i % 2 == 0:  # i = 2, 4, 6, 8 ...
            print()