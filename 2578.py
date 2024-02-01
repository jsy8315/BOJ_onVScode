import sys

A = [0] * 25

for i in range(5):
    K = list(map(int, sys.stdin.readline().split()))
    for j in range(5):
        A[(i * 5) + j] = K[j]

B = [0] * 25

for i in range(5):
    K = list(map(int, sys.stdin.readline().split()))
    for j in range(5):
        B[(i * 5) + j] = K[j]

for i in range(25): #B부터 부르기 시작
    for j in range(25):
        if B[i] == A[j]:
            A[j] = 0
    cnt = 0
    if (A[0], A[5], A[10], A[15], A[20] == 0):
        cnt += 1
        if cnt == 3:
            print(i + 1)
            break
    elif (A[1] == 0 and A[6] == 0 and A[11] == 0 and A[16] == 0 and A[21] == 0):
        cnt += 1
        if cnt == 3:
            print(i + 1)
            break
    elif (A[2] == 0 and A[7] == 0 and A[12] == 0 and A[17] == 0 and A[22] == 0):
        cnt += 1
        if cnt == 3:
            print(i + 1)
            break
    elif (A[3] == 0 and A[8] == 0 and A[13] == 0 and A[18] == 0 and A[23] == 0):
        cnt += 1
        if cnt == 3:
            print(i + 1)
            break
    elif (A[4] == 0 and A[9] == 0 and A[14] == 0 and A[19] == 0 and A[24] == 0):
        cnt += 1
        if cnt == 3:
            print(i + 1)
            break
    elif (A[0] == 0 and A[1] == 0 and A[2] == 0 and A[3] == 0 and A[4] == 0):
        cnt += 1
        if cnt == 3:
            print(i + 1)
            break
    elif (A[5] == 0 and A[6] == 0 and A[7] == 0 and A[8] == 0 and A[9] == 0):
        cnt += 1
        if cnt == 3:
            print(i + 1)
            break
    elif (A[10] == 0 and A[11] == 0 and A[12] == 0 and A[13] == 0 and A[14] == 0):
        cnt += 1
        if cnt == 3:
            print(i + 1)
            break
    elif (A[15] == 0 and A[16] == 0 and A[17] == 0 and A[18] == 0 and A[19] == 0):
        cnt += 1
        if cnt == 3:
            print(i + 1)
            break
    elif (A[20] == 0 and A[21] == 0 and A[22] == 0 and A[23] == 0 and A[24] == 0):
        cnt += 1
        if cnt == 3:
            print(i + 1)
            break
    elif (A[0] == 0 and A[6] == 0 and A[12] == 0 and A[18] == 0 and A[24] == 0):
        cnt += 1
        if cnt == 3:
            print(i + 1)
            break
    elif (A[4] == 0 and A[8] == 0 and A[12] == 0 and A[16] == 0 and A[20] == 0):
        cnt += 1
        if cnt == 3:
            print(i + 1)
            break