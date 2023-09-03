import sys

sys.stdin = open("input.txt")

N = int(input())

for i in range(N):
    count = 0
    s1 = input()
    for s in s1:
        if s == "(":
            count += 1
        if s == ")":
            count -= 1
        if count < 0:
            break
    if count == 0:
        print("YES")
    else:
        print("NO")