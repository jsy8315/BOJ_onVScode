import sys

N, M, R = map(int, sys.stdin.readline().split())

A = [0 for _ in range(N)]

for i in range(N):
    A[i] = list(map(int, sys.stdin.readline().split()))

emp = [0 for _ in range(N)]

for i in range(N):
    emp[i] = [0 for _ in range(M)]

# 껍질 수 
snail = min(N, M) // 2


def rotate(N, M):
    for i in range(N):
        for j in range(M):
            emp[i][j] = 0
            
    for k in range(snail):
        for i in range(k, N - k):
            for j in range(k, M - k):
                if i == k and j != k:
                    emp[i][j - 1] = A[i][j]
                if i != N - 1 - k and j == k:
                    emp[i + 1][j] = A[i][j]
                if i == N - 1 - k and j != M - 1 - k:
                    emp[i][j + 1] = A[i][j]
                if i != k and j == M - 1 - k:
                    emp[i - 1][j] = A[i][j]
    
    for i in range(N):
        for j in range(M):
            A[i][j] = emp[i][j]



for i in range(R):
    rotate(N, M)

for i in range(N):
    print(emp[i])


