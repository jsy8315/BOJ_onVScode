import sys

S = list(sys.stdin.readline().strip())
S.append(" ")

checkTag = 0
word = []
justword = []

while len(S) != 0:
    if S[0] == "<":
        checkTag = 1
        for i in range(len(justword)):
            word.append(justword.pop())
        
        justword.append(S.pop(0))

    elif S[0] == ">":
        checkTag = 0
        justword.append(S.pop(0))
        for i in range(len(justword)):
            word.append(justword.pop(0))

    elif S[0] == " " and checkTag == 0:
        for i in range(len(justword)):
            word.append(justword.pop())
        word.append(" ")
        S.pop(0)

    elif S[0] == " " and len(S) == 1:
        for i in range(len(justword)):
            word.append(justword.pop())
        word.append(" ")
        S.pop(0)

    else:
        justword.append(S.pop(0))

for i in range(len(word)):
    if i != len(word) - 1:
        print(word[i], end = "")
    else:
        print(word[i])

