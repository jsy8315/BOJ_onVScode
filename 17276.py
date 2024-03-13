import sys

T = int(sys.stdin.readline())

tot = []

for i in range(T):
    # 줄 수, 회전 각도
    n, d = map(int, sys.stdin.readline().split())
    
    arr = []

    for j in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    
    # 예제 배열
    # arr의 값
    # [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], 
    # [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

    # 빈 배열도 있어야 됨
    # emptyArr = [[0] * n for _ in range(n)]    생각해보니 빈 배열보다 걍 arr 복붙하면 될듯?
    # emptyArr = arr 이렇게 복사하니 안됨, 배열 하나 하나 넣어주자
    
    emptyArr = [[0] * n for _ in range(n)] 

    for j in range(n):
        for k in range(n):
            emptyArr[j][k] = arr[j][k]
    # 요소 하나 하나 를 넣어주는 식으로 하니까 되네? 왜 그럴까?

    centerNum = n // 2

    # 선 별 위치
    '''
    서북대각선        [k][k]
    북선            [k][centerNum]
    동북대각선        [k][n - 1- k]
    동선            [centerNum][n - 1 - k]
    남동대각선        [n - 1 - k][n - 1 - k]
    남선            [n - 1 - k][centerNum]
    남서대각선        [n - 1 - k][k]
    서선            [centerNum][k]
    '''

    if d == 45 or d == -315:       
        for k in range(centerNum):
            # 서북 대각선 > 북선
            emptyArr[k][centerNum] = arr[k][k]
            # 북 선 > 동북 대각선
            emptyArr[k][n - 1 - k] = arr[k][centerNum]
            # 동북 대각선 > 동 선
            emptyArr[centerNum][n - 1 - k] = arr[k][n - 1 - k]            
            # 동 선 > 남동 대각선
            emptyArr[n - 1 - k][n - 1 - k] = arr[centerNum][n - 1 - k]
            # 남동 대각선 > 남 선
            emptyArr[n - 1 - k][centerNum] = arr[n - 1 - k][n - 1 - k]
            # 남 선 > 남서 대각선
            emptyArr[n - 1 - k][k] = arr[n - 1 - k][centerNum]
            # 남서 대각선 > 서선
            emptyArr[centerNum][k] = arr[n - 1 - k][k]
            # 서 선 > 서북 대각선
            emptyArr[k][k] = arr[centerNum][k]
    elif d == 90 or d == - 270:
        for k in range(centerNum):
            # 서북 대각선 > 동북 대각선
            emptyArr[k][n - 1- k] = arr[k][k]
            # 북 선 > 동선
            emptyArr[centerNum][n - 1 - k] = arr[k][centerNum]
            # 동북 대각선 > 남동 대각선
            emptyArr[n - 1 - k][n - 1 - k] = arr[k][n - 1 - k]            
            # 동 선 > 남선
            emptyArr[n - 1 - k][centerNum] = arr[centerNum][n - 1 - k]
            # 남동 대각선 > 남서 대각선
            emptyArr[n - 1 - k][k] = arr[n - 1 - k][n - 1 - k]
            # 남 선 > 서선
            emptyArr[n - 1 - k][k] = arr[n - 1 - k][centerNum]
            # 남서 대각선 > 서북 대각선
            emptyArr[centerNum][k] = arr[n - 1 - k][k]
            # 서 선 > 북선
            emptyArr[k][centerNum] = arr[centerNum][k]
    elif d == 135 or d == -225:
        for k in range(centerNum):
            # 서북 대각선 > 동선
            emptyArr[centerNum][n - 1 - k] = arr[k][k]
            # 북 선 > 남동 대각선
            emptyArr[n - 1 - k][n - 1 - k] = arr[k][centerNum]
            # 동북 대각선 > 남선
            emptyArr[n - 1 - k][centerNum] = arr[k][n - 1 - k]            
            # 동선 > 남서 대각선
            emptyArr[n - 1 - k][k] = arr[centerNum][n - 1 - k]
            # 남동 대각선 > 서 선
            emptyArr[centerNum][k] = arr[n - 1 - k][n - 1 - k]
            # 남 선 > 서북 대각선
            emptyArr[k][k] = arr[n - 1 - k][centerNum]
            # 남서 대각선 > 북선
            emptyArr[k][centerNum] = arr[n - 1 - k][k]
            # 서 선 > 동북 대각선
            emptyArr[k][n - 1- k] = arr[centerNum][k]
    elif d == 180 or d == -180:
        for k in range(centerNum):
            # 서북 대각선 > 남동 대각선
            emptyArr[n - 1 - k][n - 1 - k] = arr[k][k]
            # 북 선 > 남 선
            emptyArr[n - 1 - k][centerNum] = arr[k][centerNum]
            # 동북 대각선 > 남서 대각선
            emptyArr[n - 1 - k][k] = arr[k][n - 1 - k]            
            # 동선 > 서선
            emptyArr[centerNum][k] = arr[centerNum][n - 1 - k]
            # 남동 대각선 > 서북 대각선
            emptyArr[k][k] = arr[n - 1 - k][n - 1 - k]
            # 남 선 > 북 선
            emptyArr[k][centerNum] = arr[n - 1 - k][centerNum]
            # 남서 대각선 > 동북 대각선
            emptyArr[k][n - 1- k] = arr[n - 1 - k][k]
            # 서 선 > 동 선
            emptyArr[centerNum][n - 1 - k] = arr[centerNum][k]
    elif d == 225 or d == -135:
        for k in range(centerNum):
            # 서북 대각선 > 남 선
            emptyArr[n - 1 - k][centerNum] = arr[k][k]
            # 북 선 > 남서 대각선
            emptyArr[n - 1 - k][k] = arr[k][centerNum]
            # 동북 대각선 > 서 선
            emptyArr[centerNum][k] = arr[k][n - 1 - k]            
            # 동선 > 서북 대각선
            emptyArr[k][k] = arr[centerNum][n - 1 - k]
            # 남동 대각선 > 북 선
            emptyArr[k][centerNum] = arr[n - 1 - k][n - 1 - k]
            # 남 선 > 동북 대각선
            emptyArr[k][n - 1- k] = arr[n - 1 - k][centerNum]
            # 남서 대각선 > 동 선
            emptyArr[centerNum][n - 1 - k] = arr[n - 1 - k][k]
            # 서 선 > 남동 대각선
            emptyArr[n - 1 - k][n - 1 - k] = arr[centerNum][k]
    elif d == 270 or d == -90:
        for k in range(centerNum):
            # 서북 대각선 > 남서 대각선
            emptyArr[n - 1 - k][k] = arr[k][k]
            # 북 선 > 서 선
            emptyArr[centerNum][k] = arr[k][centerNum]
            # 동북 대각선 > 서북 대각선
            emptyArr[k][k] = arr[k][n - 1 - k]            
            # 동선 > 북 선
            emptyArr[k][centerNum] = arr[centerNum][n - 1 - k]
            # 남동 대각선 > 동북 대각선
            emptyArr[k][n - 1- k] = arr[n - 1 - k][n - 1 - k]
            # 남 선 > 동 선
            emptyArr[centerNum][n - 1 - k] = arr[n - 1 - k][centerNum]
            # 남서 대각선 > 남동 대각선
            emptyArr[n - 1 - k][n - 1 - k] = arr[n - 1 - k][k]
            # 서 선 > 남 선
            emptyArr[n - 1 - k][centerNum] = arr[centerNum][k]
    elif d == 315 or d == -45:
        for k in range(centerNum):
            # 서북 대각선 > 서 선
            emptyArr[centerNum][k] = arr[k][k]
            # 북 선 > 서북 대각선
            emptyArr[k][k] = arr[k][centerNum]
            # 동북 대각선 > 북 선
            emptyArr[k][centerNum] = arr[k][n - 1 - k]            
            # 동선 > 동북 대각선
            emptyArr[k][n - 1- k]= arr[centerNum][n - 1 - k]
            # 남동 대각선 > 동 선
            emptyArr[centerNum][n - 1 - k] = arr[n - 1 - k][n - 1 - k]
            # 남 선 > 남동 대각선
            emptyArr[n - 1 - k][n - 1 - k] = arr[n - 1 - k][centerNum]
            # 남서 대각선 > 남 선
            emptyArr[n - 1 - k][centerNum] = arr[n - 1 - k][k]
            # 서 선 > 남서 대각선
            emptyArr[n - 1 - k][k] = arr[centerNum][k]
    else: # 360니까 그대로 출력
        emptyArr = arr

    tot.append(emptyArr)


for i in range(T):
    for j in range(len(tot[i])):
        for k in range(len(tot[i])):
            if k != len(tot[i]) - 1:
                print(tot[i][j][k], end = " ")
            else:
                print(tot[i][j][k])                
            
