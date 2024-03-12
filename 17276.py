import sys

T = int(sys.stdin.readline())

for i in range(T):
    # 줄 수, 회전 각도
    n, d = map(int, sys.stdin.readline().split())
    arr = [0 for _ in range(n)]

    for j in range(n):
        arr[i] = list(map(int, sys.stdin.readline().split()))

    if d == 45 or d == -315:
        #대각선부터
        print()
    elif d == 90 or d == - 270:
        print()
    elif d == 135 or d == -225:
        print()
    elif d == 180 or d == -180:
        print()
    elif d == 225 or d == -135:
        print()
    elif d == 270 or d == -90:
        print()
    elif d == 315 or d == -45:
        print()
    else:
        print()