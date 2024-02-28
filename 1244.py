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
            for i in range(n):
                if givenNum - i == 0 or givenNum + i == n + 1:
                    break
                elif i == 0:
                    if a[givenNum - 1] == 0:
                        a[givenNum - 1] = 1
                    else:
                        a[givenNum - 1] = 0
                else:
                    if a[givenNum - 1 - i] == a[givenNum - 1 + i]:
                        if a[givenNum - 1 - i] == 0:
                            a[givenNum - 1 - i] = 1
                            a[givenNum - 1 + i] = 1
                        else:
                            a[givenNum - 1 - i] = 0
                            a[givenNum - 1 + i] = 0   
                    else:
                        break                        


# 성별, 받은 수
for _ in range(num_student):
    b = list(map(int, sys.stdin.readline().split()))
    sex = b[0]
    givenNum = b[1]
    #print("성별, 스위치의 개수 : %d, %d"%(sex, givenNum))
    switch(sex, givenNum)


#한줄에 20개씩 출력
if n < 21:
    for i in range(n):
        if i != n - 1:
            print(a[i], end=' ')
        else:
            print(a[i])            
elif 21 <= n < 41:
    for i in range(20):
        if i != 19:
            print(a[i], end=' ')
        else:
            print(a[i])
    for i in range(20, n):
        if i != n - 1:
            print(a[i], end=' ')
        else:
            print(a[i])
elif 41 <= n < 61:
    for i in range(20):
        if i != 19:
            print(a[i], end=' ')
        else:
            print(a[i])
    for i in range(20, 40):
        if i != 39:
            print(a[i], end=' ')
        else:
            print(a[i])
    for i in range(40, n):
        if i != n - 1:
            print(a[i], end=' ')
        else:
            print(a[i])
elif 61 <= n < 81:
    for i in range(20):
        if i != 19:
            print(a[i], end=' ')
        else:
            print(a[i])
    for i in range(20, 40):
        if i != 39:
            print(a[i], end=' ')
        else:
            print(a[i])
    for i in range(40, 60):
        if i != 59:
            print(a[i], end=' ')
        else:
            print(a[i])
    for i in range(60, n):
        if i != n - 1:
            print(a[i], end=' ')
        else:
            print(a[i])        
else:
    for i in range(20):
        if i != 19:
            print(a[i], end=' ')
        else:
            print(a[i])
    for i in range(20, 40):
        if i != 39:
            print(a[i], end=' ')
        else:
            print(a[i])
    for i in range(40, 60):
        if i != 59:
            print(a[i], end=' ')
        else:
            print(a[i])
    for i in range(60, 80):
        if i != 79:
            print(a[i], end=' ')
        else:
            print(a[i])
    for i in range(80, n):
        if i != n - 1:
            print(a[i], end=' ')
        else:
            print(a[i])  
