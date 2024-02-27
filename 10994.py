#백준 10994

import sys

n = int(sys.stdin.readline())
stars = [[' ' for _ in range(4 * n - 3)] for _ in range(4 * n - 3)]

def fill_star(n, x, y):
    if n == 1:
        stars[y][x] = '*'
        return
    
    length = 4 * n - 3

    for i in range(length):
        stars[y][x + i] = '*'
        stars[y + i][x] = '*'
        stars[y + length - 1][x + i] = '*'
        stars[y + i][x + length - 1] = '*'

    fill_star(n - 1, x + 2, y + 2)

fill_star(n, 0, 0)

for i in stars:
    print(''.join(i))