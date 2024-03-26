# 백준 15787

import sys

N, M = map(int, sys.stdin.readline().split())

# N은 기차의 수, M은 명령의 수
train = [[0] * 20 for _ in range(N)]
order = [[0] for _ in range(M)]


for i in range(M):
    order[i] = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    target_train = 0
    target_train_num = order[i][1] - 1  #1을 빼줘야 0~ 이 된다
    if order[i][0] == 1:
        seat_num = order[i][2] - 1
        train[target_train_num][seat_num] = 1
    if order[i][0] == 2:
        seat_num = order[i][2] - 1
        train[target_train_num][seat_num] = 0
    if order[i][0] == 3:
        train[target_train_num]