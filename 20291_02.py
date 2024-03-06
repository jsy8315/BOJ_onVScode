import sys

N = int(sys.stdin.readline())

arr = []
dict = {}

for i in range(N):
    file = sys.stdin.readline().strip().split('.')
    arr.append(file[1])

print(arr)

for i in arr:
    if dict.get(i): #dict에 arr[i]가 존재하면
        dict[i] += 1
    else:
        dict[i] = 1

dict = sorted(dict.items())
print(dict)

for i, j in dict:
    print(i, j)