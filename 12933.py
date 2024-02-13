# 백준 12933

import sys

A = list(map(str, sys.stdin.readline().strip()))
print(A)
print(len(A))

sample = ['q', 'u', 'a', 'c', 'k']

for i in range(1, len(A)):
    if A[i] == 'q':
        