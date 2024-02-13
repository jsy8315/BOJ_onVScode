import sys

A = [0] * 25

for i in range(5):
    K = list(map(int, sys.stdin.readline().split()))
    for j in range(5):
        A[i * 5 + j] = K[j]

B = [0] * 25

for i in range(5):
    K = list(map(int, sys.stdin.readline().split()))
    for j in range(5):
        B[i * 5 + j] = K[j]

# 빙고가 되는 경우의 수는 12가지
# 가로 5개, 세로 5개, 대각선 2개, 총 12개

# 풀이 대충 보니까 다 빡구현한듯
# 일단 사회자가 부른 수를 0으로 만들고
# 0으로 만들때마다 빙고 경우의 수 돌려서 빙고면 cntBingo += 1한 다음
# cntBingo가 3이 되면 시마이

bingo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#가로 / 세로 / 대각선

for i in range(25):
    for j in range(25):
        if sum(bingo) != 3:
            if B[i] == A[j]:
                A[j] = 0
            if A[0] + A[1] + A[2] + A[3] + A[4] == 0:
                bingo[0] = 1
                if sum(bingo) == 3:
                    print(i + 1)
                    break
            if A[5] + A[6] + A[7] + A[8] + A[9] == 0:
                bingo[1] = 1
                if sum(bingo) == 3:
                    print(i + 1)
                    break 
            if A[10] + A[11] + A[12] + A[13] + A[14] == 0:
                bingo[2] = 1
                if sum(bingo) == 3:
                    print(i + 1) 
                    break
            if A[15] + A[16] + A[17] + A[18] + A[19] == 0:
                bingo[3] = 1
                if sum(bingo) == 3:
                    print(i + 1)
                    break
            if A[20] + A[21] + A[22] + A[23] + A[24] == 0:
                bingo[4] = 1
                if sum(bingo) == 3:
                    print(i + 1) 
                    break
            if A[0] + A[5] + A[10] + A[15] + A[20] == 0:
                bingo[5] = 1
                if sum(bingo) == 3:
                    print(i + 1)
                    break      
            if A[1] + A[6] + A[11] + A[16] + A[21] == 0:
                bingo[6] = 1
                if sum(bingo) == 3:
                    print(i + 1)
                    break
            if A[2] + A[7] + A[12] + A[17] + A[22] == 0:
                bingo[7] = 1
                if sum(bingo) == 3:
                    print(i + 1) 
                    break
            if A[3] + A[8] + A[13] + A[18] + A[23] == 0:
                bingo[8] = 1
                if sum(bingo) == 3:
                    print(i + 1)
                    break
            if A[4] + A[9] + A[14] + A[19] + A[24] == 0:
                bingo[9] = 1
                if sum(bingo) == 3:
                    print(i + 1)
                    break
            if A[0] + A[6] + A[12] + A[18] + A[24] == 0:
                bingo[10] = 1
                if sum(bingo) == 3:
                    print(i + 1)
                    break
            if A[4] + A[8] + A[12] + A[16] + A[20] == 0:
                bingo[11] = 1
                if sum(bingo) == 3:
                    print(i + 1)
                    break
        else:
            break