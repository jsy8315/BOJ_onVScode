# 백준 9081

import sys

T = int(sys.stdin.readline())

for i in range(T):
    word = list(map(str, sys.stdin.readline().strip()))
    n_word = len(word)
    for j in range(n_word):
        word[j] = ord(word[j])

    
