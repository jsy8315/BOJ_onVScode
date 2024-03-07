import sys

S = sys.stdin.readline().strip()

print(S)
print(len(S))
print(type(S))

tagNum = 0  #태그의 갯수

for i in range(len(S)):
    if S[i] == "<":
        tagNum += 1

print(tagNum)

r = ["a" for _ in range(len(S))]
print(r)

checkTag = 0

for i in range(len(S)):
    if S[i] == '<':
        checkTag = 1
        r[i] = S[i]
    if checkTag == 1:
        r[i] = S[i]
    if S[i] == '>':
        checkTag = 0
        r[i]


