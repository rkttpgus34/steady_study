import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())

for i in range(n):
    stack = []
    arr = input()
    for j in arr:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")