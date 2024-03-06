import sys

N = int(sys.stdin.readline())

A = [[0, 1] for _ in range(N)]

for i in range(N):
    A[i] = sys.stdin.readline().split('.')

for i in range(N):
    A[i][1] = A[i][1][:-1]

outPut = [[0, 1] for _ in range(N)]
outPut[0][0] = A[0][1]

for i in range(1, N):
    for j in range(i):
        if A[i][1] == outPut[j][0]:
            outPut[j][1] += 1
            break
        if j == i - 1 and A[i][1] != outPut[j][0]:
            outPut[i][0] = A[i][1]

finalOutput = []

for i in range(N):
    if type(outPut[i][0]) != int:
        finalOutput.append(outPut[i][0])

finalOutput = sorted(finalOutput)

for i in range(len(finalOutput)):
    for j in range(N):
        if finalOutput[i] == outPut[j][0]:
            print(finalOutput[i] + " " + str(outPut[j][1]))