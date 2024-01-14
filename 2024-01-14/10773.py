import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    a = int(input())
    if a:
        stack.append(a)
    else:
        if stack:
            stack.pop()
        else:
            stack.append(a)
print(sum(stack))
    