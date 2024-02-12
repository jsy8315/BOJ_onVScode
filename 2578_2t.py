import sys

A = [0] * 5

for i in range(5):
    A[i] = list(map(int, sys.stdin.readline().split()))

print(A)

B = [0] * 25

for i in range(5):
    K = list(map(int, sys.stdin.readline().split()))
    for j in range(5):
        B[i * 5 + j] = K[j]

print(B)

