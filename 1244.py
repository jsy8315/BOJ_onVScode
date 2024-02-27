import sys

n = int(sys.stdin.readline())   # 스위치 개수
a =  list(map(int, sys.stdin.readline().split()))   # 각 스위치의 상태
num_student = int(sys.stdin.readline())     # 학생수

# 이번엔 함수를 정해서 해보자
def switch(sex, givenNum):
    if sex == 1:
        for i in range(n):
            if (i + 1) % givenNum == 0:
                if a[i] == 0:
                    a[i] = 1
                else:
                    a[i] = 0
    else:
        if givenNum == 1:
            if a[0] == 0:
                a[0] = 1
            else:
                a[0] = 0
        elif givenNum == n:
            if a[n - 1] == 0:
                a[n - 1] = 1
            else:
                a[n - 1] = 0
        else:
            for i in range(1, n):
                if givenNum - i == 0 or givenNum + i == n + 1:
                    break
                else:
                    if a[givenNum - i] == a[givenNum + i]:
                        if a[givenNum - i] == 0:
                            a[givenNum - i] = 1
                            a[givenNum + i] = 1
                        else:
                            a[givenNum - i] = 0
                            a[givenNum + i] = 0                           

    print(a)

# 성별, 받은 수
for i in range(num_student):
    a = list(map(int, sys.stdin.readline().split()))
    sex = a[0]
    givenNum = a[1]
    switch(sex, givenNum)