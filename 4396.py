import sys

n = int(sys.stdin.readline())
mine = [[0] for _ in range(n)]
opened = [[0] for _ in range(n)]

for i in range(n):
    mine[i] = list(map(str, sys.stdin.readline().strip()))

for i in range(n):
    opened[i] = list(map(str, sys.stdin.readline().strip()))

print(mine)
print(opened)

output = [[0] * n for _ in range(n)]
print(output)

if n != 1:
    for i in range(n):
        for j in range(n):
            if opened[i][j] == ".":
                output[i][j] = "."
            else:
                if i == 0 and j == 0:
                    cnt = 0
                    if mine[0][0] == "*":
                        cnt += 1
                    if mine[0][1] == "*":
                        cnt += 1
                    if mine[1][0] == "*":
                        cnt += 1
                    if mine[1][1] == "*":
                        cnt += 1
                    output[0][0] = cnt
                elif i == 0 and j == n - 1 :
                    cnt = 0
                    if mine[0][n - 1] == "*":
                        cnt += 1
                    if mine[0][n - 2] == "*":
                        cnt += 1
                    if mine[1][n - 1] == "*":
                        cnt += 1
                    if mine[1][n - 2] == "*":
                        cnt += 1
                    output[0][0] = cnt
                elif i == n - 1 and j == 0:
                    cnt = 0
                    if mine[n - 1][0] == "*":
                        cnt += 1
                    if mine[n - 1][1] == "*":
                        cnt += 1
                    if mine[n - 2][0] == "*":
                        cnt += 1
                    if mine[n - 2][1] == "*":
                        cnt += 1
                    output[0][0] = cnt
                elif i == n - 1 and j == n - 1:
                    cnt = 0
                    if mine[n - 1][n - 1] == "*":
                        cnt += 1
                    if mine[n - 1][n - 2] == "*":
                        cnt += 1
                    if mine[n - 2][n - 1] == "*":
                        cnt += 1
                    if mine[n - 1][n - 1] == "*":
                        cnt += 1
                    output[0][0] = cnt
                elif i == 0 and ((j != 0) or (j != n - 1)):
                    cnt = 0
                    if mine[0][j] == "*":
                        cnt += 1
                    if mine[0][j - 1] == "*":
                        cnt += 1
                    if mine[0][j + 1] == "*":
                        cnt += 1
                    if mine[1][j] == "*":
                        cnt += 1
                    if mine[1][j - 1] == "*":
                        cnt += 1
                    if mine[1][j + 1] == "*":
                        cnt += 1
                    output[0][j] = cnt
                elif i == n - 1 and ((j != 0) or (j != n - 1)):
                    cnt = 0
                    if mine[n - 1][j] == "*":
                        cnt += 1
                    if mine[n - 1][j - 1] == "*":
                        cnt += 1
                    if mine[n - 1][j + 1] == "*":
                        cnt += 1
                    if mine[n - 2][j] == "*":
                        cnt += 1
                    if mine[n - 2][j - 1] == "*":
                        cnt += 1
                    if mine[n - 2][j + 1] == "*":
                        cnt += 1
                    output[n - 1][j] = cnt
                elif j == 0 and ((i != 0) or (i != n - 1)):
                    cnt = 0
                    if mine[i][0] == "*":
                        cnt += 1
                    if mine[i - 1][0] == "*":
                        cnt += 1
                    if mine[i + 1][0] == "*":
                        cnt += 1
                    if mine[i][1] == "*":
                        cnt += 1
                    if mine[i - 1][1] == "*":
                        cnt += 1
                    if mine[i + 1][1] == "*":
                        cnt += 1
                    output[i][0] = cnt
                elif j == n - 1 and ((i != 0) or (i != n - 1)):
                    cnt = 0
                    if mine[i][n - 1] == "*":
                        cnt += 1
                    if mine[i - 1][n - 1] == "*":
                        cnt += 1
                    if mine[i + 1][n - 1] == "*":
                        cnt += 1
                    if mine[i][n - 2] == "*":
                        cnt += 1
                    if mine[i - 1][n - 2] == "*":
                        cnt += 1
                    if mine[i + 1][n - 2] == "*":
                        cnt += 1
                    output[i][n - 1] = cnt
                else:
                    cnt = 0
                    if mine[i - 1][j - 1] == "*":
                        cnt += 1
                    if mine[i - 1][j] == "*":
                        cnt += 1
                    if mine[i - 1][j + 1] == "*":
                        cnt += 1
                    if mine[i][j - 1] == "*":
                        cnt += 1
                    if mine[i][j] == "*":
                        cnt += 1
                    if mine[i][j + 1] == "*":
                        cnt += 1
                    if mine[i + 1][j - 1] == "*":
                        cnt += 1
                    if mine[i + 1][j] == "*":
                        cnt += 1
                    if mine[i + 1][j + 1] == "*":
                        cnt += 1
                    output[i][j] = cnt
else:
    if opened[0][0] == ".":
        output[0][0] = "."
    else:
        if mine[0][0] == "*":
            output[0][0] = 1
        else:
            output[0][0] = 1

print(output)

for i in range(n):
    finalOutput = []
    for j in range(n):
        finalOutput.append(str(output[i][j]))

    print(finalOutput, end='')