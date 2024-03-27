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
    # 명령의 종류에서 "i번째"라고 하니까, 1을 빼주면 좀 더 편리하다
    target_train_num = order[i][1] - 1 

    if order[i][0] == 1:
        seat_num = order[i][2] - 1 # 마찬가지로 x번째니까 1을 빼주면 편리함
        train[target_train_num][seat_num] = 1

    elif order[i][0] == 2:
        seat_num = order[i][2] - 1
        train[target_train_num][seat_num] = 0

    elif order[i][0] == 3:
        train[target_train_num].pop()
        train[target_train_num].insert(0, 0)

    elif order[i][0] == 4:
        train[target_train_num].pop(0)
        train[target_train_num].append(0)

'''
시간초과로 삭제

# 건넌 기차의 수 (첫번째 열차는 일단 갈 수 있으니 1부터 시작)
crossed_train_num = 1

crossed_train_check = 0

for i in range(1, N):
    crossed_train_check = 0
    for j in range(0, i):
        if train[i] == train[j]:
            crossed_train_check = 1
    
    if crossed_train_check == 0:
        crossed_train_num += 1

print(crossed_train_num)
'''

unique_trains = set(tuple(train[i]) for i in range(N))
print(len(unique_trains))