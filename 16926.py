import sys

N, M, R = map(int, sys.stdin.readline().split())


# 껍질 수 
snail = min(N, M) // 2

def rotate():
    if