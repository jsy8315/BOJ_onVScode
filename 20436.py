import sys

#왼손, 오른손 검지손가락의 처음 위치 입력 받기
fp = list(map(str, sys.stdin.readline().split()))

#왼손 처음 위치
fpLi = 0
fpLj = 0

#오른손 처음 위치
fpRi = 0
fpRj = 0

#입력 문자열
a = str(sys.stdin.readline().strip())

keyboard = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm']
]

#처음 자판의 위치
for i in range(3):
    for j in range(len(keyboard[i])):
        if fp[0] == keyboard[i][j]:
            fpLi = i
            fpLj = j

for i in range(3):
    for j in range(len(keyboard[i])):
        if fp[1] == keyboard[i][j]:
            fpRi = i
            fpRj = j


time = 0

for i in range(len(a)):
    for j in range(3):
        for k in range(len(keyboard[j])):
            if a[i] == keyboard[j][k]:
                if  (j == 0 and 5 <= k <= 9) or (j == 1 and 5 <= k <= 8) or (j == 2 and 4 <= k <=6):
                    time += abs(fpRi - j) + abs(fpRj - k) + 1
                    fpRi = j
                    fpRj = k
                    #print(i, time)
                elif (j == 0 and k <= 4) or (j == 1 and k <= 4) or (j == 2 and k <= 3):
                    time += abs(fpLi - j) + abs(fpLj - k) + 1
                    fpLi = j
                    fpLj = k
                    #print(i, time)


print(time)

# 왼손 > 자음, 오른손 > 모음
# z o
# 1 + 1 +  2  + 4